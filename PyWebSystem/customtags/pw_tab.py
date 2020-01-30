from django.template import Template
from PyWebSystem.PyUtil.pw_logger import logmessage


def tab(context, *args, **kwargs):
    logmessage("tab", "warning")
    # context["config"]["PrimaryDict"] = "ABC"
    primaryNode = context["Primary"]
    tagname = args[1]
    filename = "C:/Users/anjaneyulu_a/Documents/Python/Apache/htdocs/WebSystem/PyWebSystem/customtags/htmltags/" + tagname + ".html"
    fileopen = open(filename, "r")
    filecode = fileopen.read()
    fileopen.close()
    # context["Primary"]["gt"]["layouttype"] = "Double"
    t = Template(filecode)
    html = t.render(context)
    context["Primary"] = primaryNode
    # logmessage("tab", "warning", context)
    return html


