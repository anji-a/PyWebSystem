from django.template import Template
from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.HtmlParse.setElementPath import setElementPath


def Accordion(context, *args, **kwargs):
    logmessage("Accordion", "warning", args)
    primaryNode = context["ElementPrimary"]
    setElementPath(context)
    tagname = args[1]
    filename = "C:/Users/anjaneyulu_a/Documents/Python/Apache/htdocs/WebSystem/PyWebSystem/customtags/htmltags/" + tagname + ".html"
    fileopen = open(filename, "r")
    filecode = fileopen.read()
    fileopen.close()
    t = Template(filecode)
    html = t.render(context)
    context["ElementPrimary"] = primaryNode
    return html