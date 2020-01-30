from django.template.loader import render_to_string
from django.template import Context, Template
from PyWebSystem.PyUtil.pw_logger import logmessage
from django.conf import settings
import os
from PyWebSystem.Samples.ElementjsSamples import gettablayoutsample
from PyWebSystem.HtmlParse.parsedicttohtml import parsedicttohtml


def render_html(context={}):
    logmessage(__name__, "warning")
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
        html = context.get("element", "")
    t = Template(html)
    c = Context(context)
    #print(c)
    # html = t.render(c)
    html = "".join([line.strip("\n\t") for line in html])
    #print(html)
    html = html.replace('"', '\\"')
    html = html.replace("/*", "\\/*")
    html = html.replace("*/", "*\\/")

    #openmodelwindow(event, displayhtml)
    #html = "openmodelwindow(event,\""+html+"\")"
    return html



