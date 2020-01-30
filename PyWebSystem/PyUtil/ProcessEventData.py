from PyWebSystem.PyUtil.ModelWindow import model_window, model_close, landing_tab
from PyWebSystem.PyUtil.pw_memory import memory_verification
from PyWebSystem.PyUtil.ExecuteCode import executeaction
from PyWebSystem.PyUtil.pw_logger import logmessage


def process_event(context={}, *args, **kwargs):
    #logmessage(__name__, "warning")
    eventdata = context.get("Config", {}).get("EventData", {})
    controldata = eventdata.get("data-controlset", {})
    actionset = controldata.get("actionset", [])
    #print(actionset, "\n", controldata)
    logmessage(__name__, "warning", controldata)
    context["root_node"] = controldata.get("root_node", "PortalNode")
    for iteration, item in enumerate(actionset):
        # controldata.get("eventtype", "") == item.get("event", ""):
        if item.get("event", "") == item.get("event", ""): # revisit the code
            eventdata = item.get("eventdata", [])
            for iteration, action in enumerate(eventdata):
                #print(action)
                if action.get("action", "") == "modelwindow":
                    model_window(context, action, params=kwargs.get("params", {}))
                elif action.get("action", "") == "memory_check" or action.get("action", "") == "refresh_memory":
                    #print(kwargs)
                    memory_verification(context, action, params=kwargs.get("params", {}))
                elif action.get("action", "") == "Close":
                    model_close(context, action, params=kwargs.get("params", {}))
                elif action.get("action", "") == "landingtab":
                    landing_tab(context, action, params=kwargs.get("params", {}))
                elif action.get("action", "") == "exeaction":
                    executeaction(context, action, params=kwargs.get("params", {}))
