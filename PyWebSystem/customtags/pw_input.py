from django.template import Template
from PyWebSystem.PyUtil.pw_logger import logmessage


def input(context, *args, **kwargs):
    logmessage(__name__, "warning", args[2])
    tagname = args[1]
    filename = "C:/Users/anjaneyulu_a/Documents/Python/Apache/htdocs/WebSystem/PyWebSystem/customtags/htmltags/" + tagname + ".html"
    fileopen = open(filename, "r")
    filecode = fileopen.read()
    fileopen.close()
    t = Template(filecode)
    html = t.render(context)
    return html
