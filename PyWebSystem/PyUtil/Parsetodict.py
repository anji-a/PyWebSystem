from PyWebSystem.HtmlParse.Parsehtmltodict import parsehtmltodict
from PyWebSystem.HtmlParse.parsedicttohtml import parsedicttohtml
from PyWebSystem.PyUtil.RenderHtmlToString import render_html
from PyWebSystem.PyUtil.pw_logger import logmessage


def parsetodict(context={}, action={}, *args, **kwargs):
    logmessage("parsetodict", "warning", context)
    eventdata = context.get("Config", {}).get("EventData", {})
    controldata = eventdata.get("data-controlset", {})
    html = controldata.get("roothtml", "")
    sourcedict = parsehtmltodict(html)
    #html = parsedicttohtml(sourcedict)
    logmessage("parsetodict", "warning", sourcedict)
    #context["element"] = html #"<div><{% autoescape off %}{% load TagUtility %}{% tag_utility pw_tag='pw_layout' scope=context%}{% endautoescape %}</div>"
    #html = render_html(context)
    #context["element_html"] = html


