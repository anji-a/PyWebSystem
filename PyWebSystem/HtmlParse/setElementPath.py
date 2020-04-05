from PyWebSystem.PyUtil.pw_logger import logmessage
import PyWebSystem.Samples.datastructure as ds
from PyWebSystem.PyUtil.DickUpdate import getkeylist, index_exists
from PyWebSystem.customtags.pw_findelement import findelement


def setElementPath(context):
    logmessage("setElementPath", "warning", [context.get("elpath", ""), context["ElementPrimary"].get("PrimaryNode", "")])
    if context.get("elpath", "") == "":
        context["ElementPrimary"]["elementpath"] = "Standard"
        context["elpath"] = "Standard"
    if context["ElementPrimary"].get("PrimaryNode", "") == "":
        context["ElementPrimary"]["elementpath"] = context.get("elpath", "")
    elif context["ElementPrimary"].get("PrimaryNode", "")[0] != ".":
        context["ElementPrimary"]["elementpath"] = context["ElementPrimary"].get("PrimaryNode", "")
    else:
        context["ElementPrimary"]["elementpath"] = context.get("elpath", "") + context["ElementPrimary"].get("PrimaryNode", "")
    definenode(context, context["ElementPrimary"]["elementpath"])


def definenode(context, path):
    keylist = getkeylist(path)
    d = context
    for index, key in enumerate(keylist):
        if isinstance(d, str):
            d = ""
        elif isinstance(d, list):
            # logmessage("setElementPath", "warning", [index_exists(d, key), "index"])
            if index_exists(d, key):
                d = d[key]
            else:
                d = d[key] = {}
        elif isinstance(d, dict) or isinstance(d, type(context)):
            re = d.get(key, None)
            # logmessage("setElementPath", "warning", key)
            if re is None:
                ele = ds.datast.get(key, None)
                # ele = findelement(context, ElementName=key)
                logmessage("definenode", "warning", [key, d])
                if ele is None:
                    d[key] = ""
                elif ele["type"] == "dict":
                    d[key] = {}
                    d = d[key]
                else:
                    d[key] = []
                    d = d[key]
            else:
                d = d.get(key, None)
    # logmessage("setElementPath", "warning", [context.get("Config", {})])
    logmessage("definenode", "warning", [context.get("Config", {}), context.get("Config", {}).get("ElementSettings", {})])
