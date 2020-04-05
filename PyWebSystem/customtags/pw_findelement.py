from django.core.cache import cache
from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.Samples.layoutSettings import layoutSettings
from PyWebSystem.db import models
import json


def findelement(context, *args, **kwargs):
    logmessage("findelement", "warning", context["ElementPrimary"])
    ElementName = kwargs.get("ElementName", "")
    # logmessage("findelement", "warning", ElementName)
    elementname = context["ElementPrimary"].get("sectionname", "")
    # elementname in ["LayoutGeneral", "LayoutPresentation", "LayoutSettings", "ActionSettingsWrapper", "LayoutAction", "LayoutActionFooter", "RunMethodSettings", "ModelWindowSettings", "ParameterSettings", "LayoutButtonsSettings"]
    if ElementName != "" or elementname != "":
        if ElementName == "" : ElementName = elementname
        logmessage("findelement", "warning", ElementName)
        cache.delete(ElementName)
        if cache.get(ElementName) is None:
            model = models.Model(tran=context.get("_transaction_", ""))
            element = {'elementclass': 'element',
                       'conditions': {'A': {'lable': 'A', 'key': 'ElementName', 'condition': '=',
                                            'value': ElementName, 'selectelement': 'true'},
                                      'B': {'lable': 'B', 'key': 'json', 'selectelement': 'true'},
                                      'C': {'lable': 'C', 'key': 'Updatedate', 'orderby': 'desc'}},
                       'logic': 'A'}
            results = model.select(element=element)
            if len(results) > 0:
                ele = json.loads(results[0].get("json", '{}'))
                cache.set(ElementName, ele)
                logmessage("findelement", "warning", ele)
                return ele
            else:
                return {}
        else:
            logmessage("findelement", "warning", cache.get(ElementName))
            return cache.get(ElementName)


    # logmessage("findelement", "warning", results)
    elementname = context["ElementPrimary"].get("sectionname", "")
    if elementname == "":
        return {"elementfind": False}
    else:
        # logmessage("findelement", "warning", layoutSettings(elementname))
        return layoutSettings(elementname)
    return {"a": "a"}
