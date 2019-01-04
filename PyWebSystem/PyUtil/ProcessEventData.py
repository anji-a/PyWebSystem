from PyWebSystem.PyUtil.ModelWindow import model_window, model_close, landing_tab
from PyWebSystem.PyUtil.pw_memory import memory_verification


def process_event(context={}, *args, **kwargs):
    eventdata = context.get("EventData", {})
    controldata = eventdata.get("data-controlset", {})
    actionset = controldata.get("actionset", [])
    #print(actionset, "\n", controldata)
    for iteration, item in enumerate(actionset):
        if controldata.get("eventtype", "") == item.get("event", ""):
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
