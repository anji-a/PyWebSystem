from django.template import Template
from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.HtmlParse.setElementPath import setElementPath
import json
from PyWebSystem.PyUtil.DickUpdate import get_dictvalue
from PyWebSystem.customtags.pw_addpath import addpath


def parsehtml(context, *args, **kwargs):
    logmessage("parsehtml", "warning", context["ElementPrimary"])
    primaryNode = context["ElementPrimary"]
    setElementPath(context)
    html = "<div data-elementname="+primaryNode.get("name", "")+" data-uitype='html' data-dirverion='"+primaryNode.get("DirVerion", "")+"' data-dir='"+primaryNode.get("Dir", "")+"' data-controltype='html' >"
    html += context["ElementPrimary"].get("html", "")
    html += "</div>"
    t = Template(html)
    html = t.render(context)
    context["ElementPrimary"] = primaryNode
    return html
