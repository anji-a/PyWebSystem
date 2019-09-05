import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PyWebSystem.settings')
#django import and setup

#from DPortal.Utility import *

import django
django.setup()

from PyWebSystem.db import models


class PyWebSystem_pyelement(models.Model):

    def __init__(self):
        models.Model.__init__(self)
        pass

    def show(self):
        print(self.__dict__)


if __name__ == '__main__':
    e = PyWebSystem_pyelement()
    e.name = 'hi'
    e.show()
    e.save()
