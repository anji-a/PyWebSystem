import json
import sys
from django.db import connection
from PyWebSystem.db.dbtransaction import Transaction
from PyWebSystem.db.TableMetaData import get_metadata_class
from PyWebSystem.db.GenerateKey import generate_key
from PyWebSystem.PyUtil.TraceException import trace_exception

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def dictfetchone(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    print(columns)
    row = cursor.fetchone()
    return dict(zip(columns, row))



class Model:

    def __init__(self, *args, **kwargs):
        #print(self.__dict__, kwargs)
        self.tran = kwargs.get("tran", None)
        pass

    def save(self, *args, **kwargs):
        # save needs to decide insert new row or update same row
        element = kwargs.get("element", {})
        conext = kwargs.get("conext", {})
        cls = element.get("elementclass", "")
        metedata = get_metadata_class(conext, cls)
        pkey = metedata.get("primarykey", "")
        cursor = self.tran.get_cursor("default")
        kwargs["cls"] = cls
        kwargs["meta"] = metedata
        #print(kwargs)
        if cursor is not None:
            keycheck = False
            for key in pkey:
                keyvalue = element.get(key, None)
                if keyvalue is None or keyvalue == "":
                    keycheck = True  # means one of the key value has Null
            if keycheck:
                self.insert(self, *args, **kwargs)
            else:
                self.update(self, *args, **kwargs)
        
    def update(self, *args, **kwargs):
        try:
            meta = kwargs["meta"]
            cursor = self.tran.get_cursor("default")
            element = kwargs.get("element", {})
            table = meta.get("tableName")
            firstarg = True
            pkey = meta.get("primarykey", "")
            executequery = True
            wherequery = ""
            updaterow = []
            if cursor is not None:
                query = "update "+table+" set "
                column_list = meta.get("columns", {})
                if not column_list:  # empty check
                    pass
                else:
                    excludelist = ["PyStream"]
                    excludelist.extend(pkey)
                    for key, value in enumerate(column_list):
                        if value in excludelist:
                            pass
                        elif firstarg:
                            query += value + "=%s"
                            updaterow.append(element.get(value, ""))
                            firstarg = False
                        else:
                            query += ","+value+"=%s"
                            updaterow.append(element.get(value, ""))
                    if "PyStream" in column_list:
                        stream = json.dumps(element, default=str)
                        stream = stream.encode('utf-8')
                        query += ", PyStream=%s"
                        updaterow.append(stream)
                    firstarg = True
                    for value in pkey:
                        if value in column_list:
                            keyvalue = element.get(value, None)
                            if keyvalue is None: # need to recheck the logic
                                executequery = False
                            elif firstarg:
                                wherequery += value+"=%s"
                                updaterow.append(keyvalue)
                                firstarg = False
                            else:
                                wherequery += "AND "+value+"=%s"
                                updaterow.append(keyvalue)
                    if executequery:
                        query += " where "+wherequery
                        print(query, updaterow)
                        cursor.execute(query, updaterow)
                        return "Success"
        except Exception:
            trace_exception(sys.exc_info())
            return None
        
    def delete(self, *args, **kwargs):

        try:
            element = kwargs.get("element", {})
            cls = element.get("PyClass")
            metedata = get_metadata_class(cls)
            pkey = metedata.get("primarykey", "")
            cursor = self.tran.get_cursor("default")
            table = metedata.get("tableName", "")
            # print(self.__dict__, args[0], kwargs)
            wherequery = ""
            queryinsert = []
            firstarg = True
            if cursor is not None:
                keycheck = False
                for key in pkey:
                    keyvalue = element.get(key, None)
                    if keyvalue is not None:
                        keycheck = True  # means one of the key value has Null
                        if firstarg:
                            firstarg = False
                            wherequery += key+"=%s"
                            queryinsert.append(keyvalue)
                        else:
                            wherequery += " AND " + key+"=%s"
                            queryinsert.append(keyvalue)
                if keycheck:
                    query = "delete from " + table + " where " + wherequery
                    print(query, queryinsert)
                    cursor.execute(query, queryinsert)
                    return "Success"
        except Exception:
            trace_exception(sys.exc_info())
            return None

    def insert(self, *args, **kwargs):
        try:
            #cls = self.__class__.__name__
            cls = kwargs["cls"]
            meta = kwargs["meta"]
            cursor = self.tran.get_cursor("default")
            element = kwargs.get("element", {})
            table = meta.get("tableName")
            pkey = meta.get("primarykey", "")
            if cursor is not None:
                # cursor.execute("SELECT * FROM public.\"" + cls + "\"")
                query = """insert into """+table+" ("
                valuequery = ""
                column_list = meta.get("columns", {})
                firstarg = True
                insertRow = {}
                if not column_list:  # empty check
                    pass
                else:
                    excludelist = ["PyStream"]
                    excludelist.extend(pkey)
                    for key, value in enumerate(column_list):
                        # print(value)
                        if value in excludelist:
                            pass
                        elif firstarg: # first argument query formation
                            firstarg = False
                            query += value
                            valuequery += "%s"
                            insertRow[value] = element.get(value, "")
                        else:
                            query += "," + value
                            valuequery += ", %s"
                            insertRow[value] = element.get(value, "")

                    for value in pkey:
                        if value is "ElementKey":
                            key = generate_key(prefix=element.get("ElementName", ""), suffix=element.get("CreateDate", ""))
                            query += ",ElementKey"
                            valuequery += ", %s"
                            insertRow["ElementKey"] = key
                        else:
                            query += ","+value
                            valuequery += ", %s"
                            key = generate_key(prefix=element.get("elementname", ""), suffix=element.get("createdate", ""))
                            insertRow[value] = key
                    if "PyStream" in column_list:
                        stream = json.dumps(insertRow, default=str)
                        stream = stream.encode('utf-8')
                        query += ",PyStream"
                        valuequery += ", %s"
                        insertRow["PyStream"] = stream
                query += ") values ("+valuequery+")"
                print(query, insertRow)
                cursor.execute(query, list(insertRow.values()))
                return "Success"
        except Exception:
            #print(Exception)
            trace_exception(sys.exc_info())
            return None

    def select(self, *args, **kwargs):
        try:
            element = kwargs.get("element", {})
            conext = kwargs.get("conext", {})
            cls = element.get("elementclass", "")
            metedata = get_metadata_class(conext, cls)
            cursor = self.tran.get_cursor("default")
            kwargs["cls"] = cls
            kwargs["meta"] = metedata
            table = metedata.get("tableName")
            query = "select "
            wherecluse = ""
            ordercluse = ""
            selectrow = []
            firstart = True
            if cursor is not None:
                if "PyStream" in metedata.get("columns", []):
                    query += "PyStream from "+table+" where "
                else:
                    columns = element.get('conditions', {})
                    for key, column in columns.items():
                        if column.get("selectelement", '') is 'true':
                            if column.get("key", '') is not '':
                                if firstart:
                                    firstart = False
                                    query += column.get("key", '')
                                else:
                                    query += ","+column.get("key", '')
                        if column.get("orderby", "") != "":
                            if ordercluse == "":
                                ordercluse = " order by " + column.get("key", '')+" "+column.get("orderby", "")
                            else:
                                ordercluse = " , " + column.get("key", '')+" "+column.get("orderby", "")
                    query += " from "+table + " where "
                logic = element.get("logic", "").split(" ")
                for val in logic:
                    if val.upper() in ["AND", "OR"]:
                        wherecluse += " " + val.upper()
                    else:
                        if val.startswith("!"):
                            conditiondict = element.get('conditions', {}).get(val, {})
                            c_key = conditiondict.get("key", '')
                            c_rel = conditiondict.get("condition", '')
                            c_val = conditiondict.get("value", '')
                            wherecluse += " NOT(" + c_key + " " + c_rel + "%s)"
                            selectrow.append(c_val)
                        else:
                            conditiondict = element.get('conditions', {}).get(val, {})
                            c_key = conditiondict.get("key", '')
                            c_rel = conditiondict.get("condition", '')
                            c_val = conditiondict.get("value", '')
                            wherecluse += " (" + c_key + " " + c_rel + "%s)"
                            selectrow.append(c_val)
                query += wherecluse
                if ordercluse is not "":
                    query += ordercluse
                if "PyStream" in metedata.get("columns", []):
                    print(query, selectrow)
                    cursor.execute(query, selectrow)
                    row = dictfetchall(cursor)
                    rowlist = []
                    for r in row:
                        pystram = str(r.get('pystream', '{}'), 'utf-8')
                        pystram = json.loads(pystram)
                        columns = element.get('conditions', {})
                        rr = {}
                        for key, column in columns.items():
                            # print(pystram, column.get("key", ''))
                            rr[column.get("key", '')] = pystram.get(column.get("key", ''), '').strip()
                        rowlist.append(rr)
                    # print(rowlist)
                    return rowlist
                else:
                    print(query, selectrow)
                    cursor.execute(query, selectrow)
                    row = dictfetchall(cursor)
                    #pystram = str(row.get('pystream', '{}'), 'utf-8')
                    #pystram = json.loads(pystram)
                    # print(row)
                    return row
        except Exception:
            trace_exception(sys.exc_info())
            return None

    def open(self,*args,**kwargs):
        try:
            element = kwargs.get("element", {})
            cls = element.get("PyClass")
            metedata = get_metadata_class(cls)
            cursor = self.tran.get_cursor("default")
            kwargs["cls"] = cls
            kwargs["meta"] = metedata
            table = metedata.get("tableName")
            query = "select PyStream from " + table + " where "
            wherecluse = ""
            selectrow = []
            if cursor is not None:
                logic = element.get("logic", "").split(" ")
                for val in logic:
                    if val.upper() in ["AND", "OR"]:
                        wherecluse += " " + val.upper()
                    else:
                        if val.startswith("!"):
                            conditiondict = element.get('conditions', {}).get(val, {})
                            c_key = conditiondict.get("key", '')
                            c_rel = conditiondict.get("condition", '')
                            c_val = conditiondict.get("value", '')
                            wherecluse += " NOT(" + c_key + " " + c_rel + "%s)"
                            selectrow.append(c_val)
                        else:
                            conditiondict = element.get('conditions', {}).get(val, {})
                            c_key = conditiondict.get("key", '')
                            c_rel = conditiondict.get("condition", '')
                            c_val = conditiondict.get("value", '')
                            wherecluse += " (" + c_key + " " + c_rel + "%s)"
                            selectrow.append(c_val)
                if wherecluse is not "":
                    query += wherecluse
                    print(query, selectrow)
                    cursor.execute(query, selectrow)
                    row = dictfetchone(cursor)
                    pystram = str(row.get('pystream', '{}'), 'utf-8')
                    pystram = json.loads(pystram)
                    #print(row)
                    return pystram
                return None
        except Exception:
            trace_exception(sys.exc_info())
            return None
