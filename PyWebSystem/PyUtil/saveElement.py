from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.db import models
import json


def saveElement(context, sourcedict):
    logmessage("saveElement", "warning", sourcedict)
    model = models.Model(tran=context.get("_transaction_", ""))
    """element = {'pyname': 'B', 'pycreatedate': '2/25/2020', 'pyupdatedate': '2/25/2020',
               'pyclass': 'element', 'pydir': 'Sample', 'pykey': '', 'elementclass': 'py_element'}
    model.save(element=element)"""
    html = sourcedict.pop("Html")
    element = {'ElementName': sourcedict.get("ElementName", ""), 'CreateDate': sourcedict.get("CreateDate", ""), 'Updatedate': sourcedict.get("Updatedate", ""), 'Html': html, 'Json': json.dumps(sourcedict), 'ElementType': sourcedict.get("ElementType", ""),
               'Dir': sourcedict.get("Dir", ""), 'DirVerion': sourcedict.get("DirVerion", ""), 'ElementKey': sourcedict.get("ElementKey", ""), 'elementclass': sourcedict.get("elementclass", "")}
    """element={'Name': 'LayoutGeneral', 'Dir': 'PyWeb', 'Version': '1:1', 'ElementType': 'Section', 'elements': [{'controlset': {}, 'controltype': 'Layout', 'columns': [{'controlset': {}, 'controltype': 'DropDown', 'property': '', 'sourcelist': '', 'Label': ''}, {'controlset': {}, 'controltype': 'DropDown', 'property': '', 'sourcelist': '', 'Label': ''}, {'controlset': {}, 'controltype': 'DropDown', 'property': '', 'sourcelist': '', 'Label': ''}, {'controlset': {}, 'controltype': 'Input', 'property': '', 'sourcelist': '', 'Label': ''}]}]}"""
    model.save(conext=context, element=element)
