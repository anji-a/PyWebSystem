from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.PyUtil.pw_extra_methods import id_generator
from django.template import Template
from PyWebSystem.HtmlParse.setElementPath import setElementPath
from PyWebSystem.customtags.pw_findelement import findelement
import json


def form(context, *args, **kwargs):
    logmessage("addsection", "warning")
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
