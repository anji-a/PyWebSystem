import os
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PyWebSystem.settings')
#django import and setup

#from DPortal.Utility import *

import django
django.setup()

from PyWebSystem.db import models
from PyWebSystem.db.dbtransaction import Transaction
from PyWebSystem.Samples.sampletouse import fun1


if __name__ == '__main__':
    fun1()
