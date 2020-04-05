from PyWebSystem.PyUtil.ModelWindow import model_window, model_close, landing_tab
from PyWebSystem.PyUtil.pw_memory import memory_verification
from PyWebSystem.PyUtil.ExecuteCode import executeaction
from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.PyUtil.refreshsection import refreshsection
from PyWebSystem.PyUtil.deleterow import deleterow
from PyWebSystem.PyUtil.addrow import addrow
from PyWebSystem.PyUtil.refreshothersection import refreshothersection
from PyWebSystem.PyUtil.previewelement import previewelement
from PyWebSystem.PyUtil.opensettings import opensettings
from PyWebSystem.PyUtil.closeTab import closeTab


def process_event(context={}, *args, **kwargs):
    logmessage("process_event", "warning", context)
    # kwargs["params"]["session"] = session  # it will used to create new Node
    eventdata = context.get("Config", {}).get("EventData", {})
    controldata = eventdata.get("data-controlset", {})
    actionset = controldata.get("actionset", [])
    context["root_node"] = controldata.get("root_node", "PortalNode")
    for iteration, item in enumerate(actionset):
        # controldata.get("eventtype", "") == item.get("event", ""):
        if controldata.get("eventtype", "") == item.get("event", ""): # revisit the code, execute actions only based on event type
            eventdata = item.get("eventdata", [])
            for iteration, action in enumerate(eventdata):
                if action.get("action", "") == "modelwindow":
                    model_window(context, action, params=kwargs.get("params", {}))
                elif action.get("action", "") == "memory_check" or action.get("action", "") == "refresh_memory":
                    memory_verification(context, action, params=kwargs.get("params", {}))
                elif action.get("action", "") == "Close":
                    model_close(context, action, params=kwargs.get("params", {}))
                elif action.get("action", "") == "landingtab":
                    landing_tab(context, action, params=kwargs.get("params", {}))
                elif action.get("action", "") == "exeaction":
                    executeaction(context, action, params=kwargs.get("params", {}))
                elif action.get("action", "") == "refreshsection":
                    refreshsection(context, action, params=kwargs.get("params", {}))
                elif action.get("action", "") == "deleterow":
                    deleterow(context, action, params=kwargs.get("params", {}))
                elif action.get("action", "") == "addrow":
                    addrow(context, action, params=kwargs.get("params", {}))
                elif action.get("action", "") == "refreshothersection":
                    refreshothersection(context, action, params=kwargs.get("params", {}))
                elif action.get("action", "") == "previewelement":
                    previewelement(context, action, params=kwargs.get("params", {}))
                elif action.get("action", "") == "opensettings":
                    opensettings(context, action, params=kwargs.get("params", {}))
                elif action.get("action", "") == "closeTab":
                    closeTab(context, action, params=kwargs.get("params", {}))
