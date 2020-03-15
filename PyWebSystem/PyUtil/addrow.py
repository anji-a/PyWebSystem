from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.PyUtil.RenderHtmlToString import render_html
from PyWebSystem.PyUtil.DickUpdate import get_dictvalue, index_exists, set_val, getkeylist


def addrow(context={}, action={}, *args, **kwargs):
    logmessage("addrow", "warning", action)
    path = action.get("actiondata", {}).get("path", "")
    rootdict = get_dictvalue(context, path)
    len = rootdict.__len__()
    action = {"index": len+1}
    logmessage("addrow", "warning", rootdict)
    if isinstance(rootdict, list):
        rootdict.append(action)
    logmessage("addrow", "warning", context.get("Config", {}).get("ElementSettings", {}))
