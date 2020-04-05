from django.template import Template
from PyWebSystem.PyUtil.pw_logger import logmessage
import json, sys


def ParseConfigToHtml(context, *args, **kwargs):
    try:
        logmessage("ParseConfigToHtml", "warning", context.get("Config", {}).get("ElementSettings", {}))
        logmessage("ParseConfigToHtml", "warning", args)
        strb = args[2]
        strb = strb[:strb.__len__() - 1]
        strb = strb[1:]
        context['ElementConfig'] = json.loads(strb)
        tagname = args[1]
        logmessage("ParseConfigToHtml", "warning", context['ElementConfig'])
        filename = "C:/Users/anjaneyulu_a/Documents/Python/Apache/htdocs/WebSystem/PyWebSystem/customtags/htmltags/" + tagname + ".html"
        fileopen = open(filename, "r")
        filecode = fileopen.read()
        fileopen.close()
        t = Template(filecode)
        # html = "{%load TagUtility%}"
        html = t.render(context)
        return html
    except:
        logmessage("ParseConfigToHtml", "error", exception=sys.exc_info())
        return ""
