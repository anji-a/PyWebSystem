from django.template import Template
from PyWebSystem.PyUtil.pw_logger import logmessage
import json


def ParseConfigToHtml(context, *args, **kwargs):
    logmessage("ParseConfigToHtml", "warning", context["Config"].get("ElementSettings", {}))
    # logmessage("ParseConfigToHtml", "warning", context)
    strb = args[2]
    strb = strb[:strb.__len__() - 1]
    strb = strb[1:]
    context['ElementConfig'] = json.loads(strb)
    tagname = args[1]
    # logmessage("ParseConfigToHtml", "warning", context)
    filename = "C:/Users/anjaneyulu_a/Documents/Python/Apache/htdocs/WebSystem/PyWebSystem/customtags/htmltags/" + tagname + ".html"
    fileopen = open(filename, "r")
    filecode = fileopen.read()
    fileopen.close()
    t = Template(filecode)
    # html = "{%load TagUtility%}"
    html = t.render(context)
    return html
