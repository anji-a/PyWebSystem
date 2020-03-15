from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.PyUtil.DickUpdate import pw_loop
import json


def defineevents(context, *args, **kwargs):
    logmessage("defineevents", "warning")
    controlset = context["ElementPrimary"].get("controlset", "")
    eventscript = ""
    if len(controlset) == 0:
        return eventscript
    else:
        # controlset = json.loads(controlset)
        for index, key, path, value in pw_loop(controlset.get("actionset", [])):
            if value.get("event", "") == "click":
                eventscript += "onclick=processeventaction(event)"
            elif value.get("event", "") == "change":
                eventscript += "onchange=processeventaction(event)"
    return eventscript
