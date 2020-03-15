from django.template import Context, Template
from PyWebSystem.PyUtil.pw_logger import logmessage
import json
from PyWebSystem.PyUtil.DickUpdate import index_exists
from PyWebSystem.customtags.pw_definePrimaryNode import definePrimaryNode
from PyWebSystem.HtmlParse.setElementPath import setElementPath


def layout(context, *args, **kwargs):
    logmessage("layout", "warning", args)
    primaryNode = context["ElementPrimary"]
    #logmessage("layout", "warning", index_exists(args, 2))
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


def staticLayout(context, *args):
    logmessage("staticLayout", "warning", args)
    if context.get("elpath", "") == "":
        context["Primary"]["elementpath"] = "Standard"
    if context["Primary"].get("PrimaryNode", "") == "":
        context["Primary"]["elementpath"] = context.get("elpath", "")
    else:
        context["Primary"]["elementpath"] = context.get("elpath", "") + context["Primary"].get("PrimaryNode", "")
    tagname = args[1]
    filename = "C:/Users/anjaneyulu_a/Documents/Python/Apache/htdocs/WebSystem/PyWebSystem/customtags/htmltags/" + tagname + ".html"
    fileopen = open(filename, "r")
    filecode = fileopen.read()
    fileopen.close()
    t = Template(filecode)
    html = t.render(context)
    return html


def dynamicLayout(context, *args):
    logmessage("dynamicLayout", "warning", args)
    conf = args[2]
    conf = conf[1:]
    conf = conf[:-1]
    confdict = json.loads(conf)
    layouthtml = "<div class='w3-container w3-card-4 w3-light-grey'>"
    if context.get("elpath", "") == "":
        context["Primary"]["elementpath"] = "Standard"
    if confdict.get("PrimaryNode", "") == "":
        elepath = context.get("elpath", "")
    elif confdict.get("PrimaryNode", "")[0] != ".":
        elepath = confdict.get("PrimaryNode", "")
    else:
        elepath= context.get("elpath", "") + confdict.get("PrimaryNode", "")
    context["Primary"] = definePrimaryNode(context, "", "", elepath)
    for key, value in enumerate(confdict.get("columns", [])):
        strval = json.dumps(value)
        if value.get("controltype", "") == "Input":
            html = '{%includeTag input "'+strval+'"%}'
        if value.get("controltype", "") == "checkbox":
            html = "<div>check box</div>"
        t = Template(html)
        layouthtml += t.render(context)
    return layouthtml+"</div>"
