from django.template import Template
from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.HtmlParse.setElementPath import setElementPath
from PyWebSystem.PyUtil.DickUpdate import get_dictvalue
from PyWebSystem.customtags.pw_addpath import addpath


def icon(context, *args, **kwargs):
    logmessage("icon", "warning", args)
    primaryNode = context["ElementPrimary"]
    setElementPath(context)
    # element = addpath(context["ElementPrimary"].get("property", ""), context["ElementPrimary"].get("elementpath", ""))
    # value = get_dictvalue(context, element)
    # context["ElementPrimary"]["value"] = value
    tagname = args[1]
    filename = "C:/Users/anjaneyulu_a/Documents/Python/Apache/htdocs/WebSystem/PyWebSystem/customtags/htmltags/" + tagname + ".html"
    fileopen = open(filename, "r")
    filecode = fileopen.read()
    fileopen.close()
    t = Template(filecode)
    html = t.render(context)
    context["ElementPrimary"] = primaryNode
    return html
