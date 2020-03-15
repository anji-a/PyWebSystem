from django.conf import settings
from PyWebSystem.db.DatabaseImport import get_database
import sys
from PyWebSystem.PyUtil.TraceException import trace_exception


class Transaction:
    _dblistcon = {}
    _cursorlist = {}

    def __init__(self):
        self._dblistcon = {}
        self._cursorlist = {}

    def get_connection(self, dbname):
        # print(self._dblist)
        if dbname in self._dblistcon:
            # print(self._dblist.get(dbname, None))
            return self._dblistcon.get(dbname, None)
        else:
            try:
                engine = settings.DATABASES["default"]["ENGINE"]
                # print(engine)
                database = get_database(engine)
                connection = database.connect(host='localhost',
                                                     database=settings.DATABASES["default"]["NAME"],
                                                     user=settings.DATABASES["default"]["USER"],
                                                     password=settings.DATABASES["default"]["PASSWORD"])
                self._dblistcon[dbname] = connection
                connection.autocommit = False
                return connection
            except Exception:
                trace_exception(sys.exc_info())
                return None

    def start_transaction(self):
        pass

    def close_transaction(self):
        #print("close_transaction")
        try:
            for key, cur in self._cursorlist.items():
                # print(cur)
                cur.close()
            for key, con in self._dblistcon.items():
                # print(con)
                if True: # need to commit based on errors
                    con.commit()
                else:
                    con.rollback()
                con.close()
        except Exception:
            print(sys.exc_info())

    def get_cursor(self, dbname):
        #print("close_transaction", dbname, self._cursorlist)
        try:
            if dbname in self._cursorlist:
                return self._cursorlist.get(dbname, None)
            else:
                db = self.get_connection(dbname)
            if db is not None:
                cur = db.cursor()
                self._cursorlist[dbname] = cur
            else:
                cur = None
            return cur
        except Exception:
            print(sys.exc_info())
            return None
