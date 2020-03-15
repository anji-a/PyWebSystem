from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.PyUtil.refreshsection import refreshsectionwrapper
from PyWebSystem.PyUtil.DickUpdate import pw_loop


def refreshothersection(context={}, action={}, *args, **kwargs):
    logmessage("refreshothersection", "warning", action)
    eventdata = action.get("actiondata", {})
    context["data_element"] = "dynamic"
    for index, key, path, value in pw_loop(eventdata):
        sectionname = value.get("refreshsection", "")
        elementid = value.get("refreshid", "")
        node = value.get("refreshnode", "")
        refreshsectionwrapper(context, node, sectionname, elementid)
