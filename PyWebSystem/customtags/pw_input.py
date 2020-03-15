from django.template import Template
from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.HtmlParse.setElementPath import setElementPath
import json
from PyWebSystem.PyUtil.DickUpdate import get_val, getkeylist, get_dictvalue
from PyWebSystem.customtags.pw_addpath import addpath


def input(context, *args, **kwargs):
    logmessage("input", "warning", context["Config"].get("ElementSettings"))
    primaryNode = context["ElementPrimary"]
    setElementPath(context)
    element = addpath(context["ElementPrimary"].get("property", ""), context["ElementPrimary"].get("elementpath", ""))
    # keylist = getkeylist(element)
    # logmessage("input", "warning", keylist)
    # value = get_val(context, keylist)
    value = get_dictvalue(context, element)
    logmessage("input", "warning", value)
    context["ElementPrimary"]["value"] = value
    tagname = args[1]
    filename = "C:/Users/anjaneyulu_a/Documents/Python/Apache/htdocs/WebSystem/PyWebSystem/customtags/htmltags/" + tagname + ".html"
    fileopen = open(filename, "r")
    filecode = fileopen.read()
    fileopen.close()
    t = Template(filecode)
    html = t.render(context)
    context["ElementPrimary"] = primaryNode
    return html


def staticinput(context, *args):
    logmessage("dynamicinput", "warning", args)
    setElementPath(context)
    tagname = args[1]
    filename = "C:/Users/anjaneyulu_a/Documents/Python/Apache/htdocs/WebSystem/PyWebSystem/customtags/htmltags/" + tagname + ".html"
    fileopen = open(filename, "r")
    filecode = fileopen.read()
    fileopen.close()
    t = Template(filecode)
    html = t.render(context)
    return html


def dynamicinput(context, *args):
    logmessage("dynamicinput", "warning", args)
    conf = args[2]
    conf = conf[1:]
    conf = conf[:-1]
    confdict = json.loads(conf)
    html = '<div>' \
           '<label>{{'+confdict.Label+'}}</label> ' \
           '<input class="w3-input w3-border" type="text" name="{{'+confdict.property+'|add_path:path}}" value="{{'+confdict.property+'|add_flower:path}}">' \
           '</div>'
    html = "abc"
    return html
