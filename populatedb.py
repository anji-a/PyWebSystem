import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PyWebSystem.settings')
#django import and setup

#from DPortal.Utility import *
from django.template import Context, Template
import django
django.setup()

from PyWebSystem.Models import PT_Element

from faker import Faker

fakegen = Faker()

def save_PyElement():
    data={}
    data['element_name'] = fakegen.name()
    data['element_createddatetime'] = fakegen.date()
    data['element_updatedatetime'] = fakegen.date()
    data['element_stream'] = fakegen.text()
    data['element_mode'] = 'Section'
    # print(str.encode(str(data)))
    pyObject = PT_Element.PTElement()
    pyObject.set_data(data=data)
    pyObject.save()

def get_PyElement():
    # pyObject=py_element
    all_objs = PTElement.objects.all()
    distinct_objs = PTElement.objects.distinct('MPM_type').values('MPM_type')
    #print(getApplicationPath())
    print(list(distinct_objs))
    #writeFile(all_objs[4].get_data())

def renderhtml():
    t = Template("{% autoescape off %}{% load TagUtility %}{%includeBlockTag Upper {'a':'b'} %}{%includeTag Upper 'abc' %}<a>end</a>{%endincludeBlockTag%}{% endautoescape %}")
    c = Context({"a": "a"})
    # print(c)
    html = t.render(c)
    print(html)

if __name__ == '__main__':
    print("Popula Script start")
    renderhtml()
    #get_PyElement()
    print("Popula Script end")