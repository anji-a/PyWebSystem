from django.template.loader import render_to_string
from django.template import Context, Template
from PyWebSystem.PyUtil.pw_logger import logmessage
from django.conf import settings
import os
from PyWebSystem.Samples.ElementjsSamples import gettablayoutsample
from PyWebSystem.HtmlParse.parsedicttohtml import parsedicttohtml


def render_html(context={}, conf={}):
    logmessage("render_html", "warning", context.get("Config", {}).get("ElementSettings", {}))
    #print("........", context.get("element", ""))
    if context.get("data_element", '') == "static":
        # html = render_to_string('PyWeb/pw_screen_render.html', context={"context": context})
        #logmessage(__name__, "warning", os.path.join(settings.HTML_DIR, context.get("element", "")+".html"))
        if os.path.exists(os.path.join(settings.HTML_DIR, context.get("element", "")+".html")):
            filename = os.path.join(settings.HTML_DIR, context.get("element", "")+".html")
            fileopen = open(filename, "r")
            html = fileopen.read()
            fileopen.close()
            #logmessage(__name__, "warning", html)
        else:
            filename = os.path.join(settings.TEMPLATE_DIR, "PyWeb"+context.get("element", "")+".html")
            fileopen = open(filename, "r")
            html = fileopen.read()
            fileopen.close()
            logmessage(__name__, "warning", "else")
        sourcedict = gettablayoutsample()
        html = parsedicttohtml(sourcedict)
    else:
        html = parsedicttohtml(conf)
        # html = context.get("element", "")
    t = Template(html)
    #if len(context["Standard"].get("Person", {})) == 0:
        #context["Standard"]["Person"] = {"anji":{"Name": "Anji"}, "adhi":{"Name": "Adhi"}}
    # if len(context["Config"].get("ElementSettings", {}).get("Action", {}).get("Actions", [])) == 0:
        # context["Config"].get("ElementSettings", {})["Action"] = {}
        # context["Config"].get("ElementSettings", {}).get("Action", {})["Actions"] = []
        # logmessage("render_html", "warning", context)
    c = Context(context)
    # print("Elements Action\n", context["Config"].get("ElementSettings", {}))
    html = t.render(c)
    html = "".join([line.strip("\n\t") for line in html])
    #print(html)
    html = html.replace('"', '\\"')
    html = html.replace("/*", "\\/*")
    html = html.replace("*/", "*\\/")

    #openmodelwindow(event, displayhtml)
    #html = "openmodelwindow(event,\""+html+"\")"
    return html



