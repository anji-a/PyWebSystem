from django.db import connection


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class Model:

    def __init__(self, *args, **kwargs):
        print(self.__dict__, "hELLO")
        pass

    def save(self):

        print(self.__dict__)
        cls = self.__class__.__name__
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM public.\""+cls+"\"")
            print(dictfetchall(cursor))
        for k, v in self.__dict__.items():
            print(k, v, cls)
        pass

    def delete(self):
        pass

    def insert(self):
        pass

    def select(self):
        pass
