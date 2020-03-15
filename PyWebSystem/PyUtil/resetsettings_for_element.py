from PyWebSystem.PyUtil.pw_logger import logmessage
import json


def resetsettings_for_element(context={}, action={}, *args, **kwargs):
    logmessage("resetsettings_for_element", "warning", context)
    config = json.dumps(context.get("Config", {}).get("ElementSettings", {}))
    id = context.get("Config", {}).get("ElementSettings", {}).get("id", "")
    context["element_html"] = "pw(event).saveelementsettings("+id+"," + config + "); closemodel(event);"
