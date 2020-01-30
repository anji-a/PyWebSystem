from PyWebSystem.PyUtil.pw_logger import logmessage
import json


def resetsettings_for_element(context={}, action={}, *args, **kwargs):
    logmessage("resetsettings_for_element", "warning", action)
    root_node = context.get("root_node", "Standard")
    context[root_node] = json.loads(action.get('config', '{}'))
