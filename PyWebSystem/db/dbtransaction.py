from django.db import connections
from django.conf import settings


class Transaction:
    _dblist = {}
    def __init__(self):
        pass

    def get_connection(self, dbname):
        if self._dblist.get(dbname):
            return self._dblist.get(dbname)
        else:
            try:
                connection = mysql.connector.connect(host='localhost',
                                                     database='Electronics',
                                                     user='pynative',
                                                     password='pynative@#29')
        return con;

    def start_transaction(self):
        pass

    def close_transaction(self):
        pass


def get_cursor(dbname):
    tran = Transaction(dbname)
    try:
        cur = tran.get_connection();

    except Exception:
        pass
    pass
