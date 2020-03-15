from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.PyUtil.RenderHtmlToString import render_html
from PyWebSystem.PyUtil.DickUpdate import get_dictvalue, index_exists


def deleterow(context={}, action={}, *args, **kwargs):
    logmessage("deleterow", "warning", action)
    path = action.get("actiondata", {}).get("path", "")
    rootnode = ""
    if path[-1] == "]":
        rootnode = path[:-3]
    deletevalue = get_dictvalue(context, rootnode)
    logmessage("deleterow", "warning", rootnode)
    index = path[-3:]
    if isinstance(deletevalue, list) and index_exists(deletevalue, int(index[1:-1])):
        logmessage("deleterow", "warning", index)
        deletevalue.pop(int(index[1:-1]))
    logmessage("deleterow", "warning", context.get("Config", {}).get("ElementSettings", {}))
