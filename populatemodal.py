import os
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PyWebSystem.settings')
#django import and setup

#from DPortal.Utility import *

import django
django.setup()

from PyWebSystem.db import models
from PyWebSystem.db.dbtransaction import Transaction

class PyWebSystem_pyelement(models.Model):

    def __init__(self, *args, **kwargs):
        # print(self.__dict__, kwargs, args)
        models.Model.__init__(self, *args, **kwargs)
        pass

    def show(self):
        print(self.__dict__)


if __name__ == '__main__':
    transaction = Transaction()
    e = PyWebSystem_pyelement(tran=transaction)
    e.name = 'hi'
    # e.show()
    #list = ["element_name", "element_createddatetime"]
    #r = e.select(column_list=list)
    #print(r)
    #list.append("element_stream")
    #r = e.select(column_list=list)
    #print(r) datetime.date(1999, 12, 3).strftime(timeformat) 'PyKey': 'Leslie Ford_Justin Glenn_David Jones'
    timeformat = "%d-%b-%y %H:%M:%S:%f"
    element = {'PyName': 8, 'PyCreateDate': datetime.date(1999, 12, 3), 'PyUpdateDate': datetime.date(1999, 12, 3),
               'PyClass': 'element', 'PyDir': 'Sample', 'PyKey': 'Brian Lawson_Jacob Woods_Julia Sellers'}
    delelement = {'PyName': 8, 'PyCreateDate': datetime.date(1999, 12, 3), 'PyUpdateDate': datetime.date(1999, 12, 3),
               'PyClass': 'element', 'PyDir': 'Sample', 'PyKey': 'Brian Lawson_Jacob Woods_Julia Sellers'}
    openelement = {'PyClass': 'element', 'conditions': {'A':{'lable': 'A', 'key': 'PyKey', 'condition': '=', 'value': 'Brian Lawson_Jacob Woods_Julia Sellers'},
                                                        'B':{'lable': 'B', 'key': 'PyClass', 'condition': '=', 'value': 'element'}}, 'logic': 'A AND B'}
    selectelements = {'PyClass': 'element', 'conditions': {
        'A': {'lable': 'A', 'key': 'PyKey', 'condition': '=', 'value': 'Brian Lawson_Jacob Woods_Julia Sellers'},
        'B': {'lable': 'B', 'key': 'PyClass', 'condition': '=', 'value': 'element'},
        'C': {'lable': 'B', 'key': 'PyName', 'condition': 'select', },
        'D': {'lable': 'B', 'key': 'PyDir', 'condition': 'select', }}, 'logic': 'A OR B'}
    # e.save(element=element)
    # r = e.open(element=openelement)
    # r = e.select(element=selectelements)
    r = e.delete(element=delelement)
    print(r)

    transaction.close_transaction()
