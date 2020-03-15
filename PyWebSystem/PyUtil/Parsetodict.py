from PyWebSystem.HtmlParse.Parsehtmltodict import parsehtmltodict
from PyWebSystem.HtmlParse.parsedicttohtml import parsedicttohtml
from PyWebSystem.PyUtil.RenderHtmlToString import render_html
from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.db import models
import json
from PyWebSystem.PyUtil.saveElement import saveElement


def parsetodict(context={}, action={}, *args, **kwargs):
    logmessage("parsetodict", "warning")
    eventdata = context.get("Config", {}).get("EventData", {})
    controldata = eventdata.get("data-controlset", {})
    html = controldata.get("roothtml", "")
    sourcedict = parsehtmltodict(html)
    # html = parsedicttohtml(sourcedict)
    logmessage("parsetodict", "warning", sourcedict)
    # saveElement(context, sourcedict)
    #context["element"] = html #"<div><{% autoescape off %}{% load TagUtility %}{% tag_utility pw_tag='pw_layout' scope=context%}{% endautoescape %}</div>"
    #html = render_html(context)
    #context["element_html"] = html


"""def saveelement(context, sourcedict):
    logmessage("parsetodict", "warning", sourcedict)
    model = models.Model(tran=context.get("_transaction_", ""))
    element = {'pyname': 'B', 'pycreatedate': '2/25/2020', 'pyupdatedate': '2/25/2020',
               'pyclass': 'element', 'pydir': 'Sample', 'pykey': '', 'elementclass': 'py_element'}
    model.save(element=element)
    element = {'ElementName': sourcedict.get("ElementName", ""), 'CreateDate': sourcedict.get("CreateDate", ""), 'Updatedate': sourcedict.get("Updatedate", ""), 'Html': sourcedict.get("Html", ""), 'Json': json.dumps(sourcedict), 'ElementType': sourcedict.get("ElementType", ""),
               'Dir': sourcedict.get("Dir", ""), 'DirVerion': sourcedict.get("DirVerion", ""), 'ElementKey': sourcedict.get("ElementKey", ""), 'elementclass': sourcedict.get("elementclass", "")}
    element={'Name': 'LayoutGeneral', 'Dir': 'PyWeb', 'Version': '1:1', 'ElementType': 'Section', 'elements': [{'controlset': {}, 'controltype': 'Layout', 'columns': [{'controlset': {}, 'controltype': 'DropDown', 'property': '', 'sourcelist': '', 'Label': ''}, {'controlset': {}, 'controltype': 'DropDown', 'property': '', 'sourcelist': '', 'Label': ''}, {'controlset': {}, 'controltype': 'DropDown', 'property': '', 'sourcelist': '', 'Label': ''}, {'controlset': {}, 'controltype': 'Input', 'property': '', 'sourcelist': '', 'Label': ''}]}]}
    model.save(conext=context, element=element)"""

