from django.template import Template
from PyWebSystem.PyUtil.pw_logger import logmessage
import json


def includescreen(context, *args, **kwargs):
    logmessage("includescreen", "warning", args[2])
    strb = args[2]
    strb =strb[:strb.__len__()-1]
    strb = strb[1:]
    context['Config']['config'] = json.loads(strb)
    tagname = args[1]
    filename = "C:/Users/anjaneyulu_a/Documents/Python/Apache/htdocs/WebSystem/PyWebSystem/customtags/htmltags/" + tagname + ".html"
    fileopen = open(filename, "r")
    filecode = fileopen.read()
    fileopen.close()
    t = Template(filecode)
    html = t.render(context)
    return html
