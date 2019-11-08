from PyWebSystem.HtmlParse.Parsehtmltodict import parsehtmltodict
from PyWebSystem.HtmlParse.parsedicttohtml import parsedicttohtml
from PyWebSystem.PyUtil.RenderHtmlToString import render_html


def parsetodict(context={}, action={}, *args, **kwargs):
    eventdata = context.get("EventData", {})
    controldata = eventdata.get("data-controlset", {})
    html = controldata.get("roothtml", "")
    sourcedict = parsehtmltodict(html)
    html = parsedicttohtml(sourcedict)
    print(html)
    context["element"] = html #"<div><{% autoescape off %}{% load TagUtility %}{% tag_utility pw_tag='pw_layout' scope=context%}{% endautoescape %}</div>"
    html = render_html(context)
    context["element_html"] = html


