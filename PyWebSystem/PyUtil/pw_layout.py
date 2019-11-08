from bs4 import BeautifulSoup
from PyWebSystem.PyUtil.pw_extra_methods import id_generator
from PyWebSystem.PyUtil.DickUpdate import list_loop, dict_loop
import json


def pw_layout(context={}, *args, **kwargs):
    """
        {% autoescape off %}{% load TagUtility %}{% tag_utility pw_tag="pw_navigation" scope=context%}{% endautoescape %}
    """
    print(".......", type(kwargs["columns"]))
    html = ""
    soup = BeautifulSoup(html, "lxml")
    dev_tag = soup.new_tag("div")
    cocumns_set = json.loads(kwargs.get("columns", "[]"))
    print(cocumns_set)
    for key, col in enumerate(cocumns_set):
        print(col)
        if col.get("controltype") == "Input":
            html = '{% autoescape off %}{% load TagUtility %}{% tag_utility pw_tag="pw_navigation" scope=context%}{% endautoescape %}'
    dev_tag.append(html)
    soup.append(dev_tag)
    return str(soup)
