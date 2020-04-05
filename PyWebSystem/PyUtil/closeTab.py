from PyWebSystem.PyUtil.pw_logger import logmessage
import PyWebSystem.PyConfig.GlobalValues as GV
import sys


def closeTab(context={}, action={}, *args, **kwargs):
    try:
        logmessage("closeTab", "warning", action)
        actiondata = action.get("actiondata", {})
        if actiondata.get("worknode", "") != "":
            del GV.session[actiondata.get("worknode", "")]  # delete work node from session
        context["element_html"] = context.get("element_html", "") + "w3closeworktab(event,\"" + actiondata.get("tabid", "") + "\",\"" + actiondata.get("tabcontentid", "") + "\")"
    except:
        logmessage("closeTab", "error", exception=sys.exc_info())
