from django.template import Context, Template
from PyWebSystem.PyUtil.pw_logger import logmessage
import json


def layout(context, *args, **kwargs):
    """
    need to render and return template code from html rule
    For now hotcode the Html
    :param context:
    :param args:
    :param kwargs:
    :return:
    """
    logmessage("layout", "warning", args)
    primaryNode = context["Primary"]
    #stra = '{"controlset": {"gt": {"layouttype": "Single", "visibility": "Always"}, "pt": {}, "at": {}}, "controltype": "Layout", "columns": [{"controlset": {}, "controltype": "Input"}]}'
    #logmessage(__name__, "warning", stra)
    #strb = args[2]
    #strb =strb[:strb.__len__()-1]
    #strb = strb[1:]
    #print(strb, stra)
    #context['config'] = json.loads(strb)
    tagname = args[1]
    filename = "C:/Users/anjaneyulu_a/Documents/Python/Apache/htdocs/WebSystem/PyWebSystem/customtags/htmltags/" + tagname + ".html"
    fileopen = open(filename, "r")
    filecode = fileopen.read()
    fileopen.close()
    #logmessage(__name__, "warning", filecode)
    t = Template(filecode)
    #c = Context(context)
    #print(c)
    html = t.render(context)
    context["Primary"] = primaryNode
    return html
