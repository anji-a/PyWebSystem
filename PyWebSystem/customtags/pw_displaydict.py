from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.PyUtil.DickUpdate import get_dictvalue, getkeylist
from PyWebSystem.PyUtil.pw_extra_methods import id_generator


def displaydict(context, *args, **kwargs):
    logmessage("displaydict", "warning", args)
    keylist = context["key"]
    #NodeName = context.get(keylist[0], {}).get("NodeName", "")
    selected_dick = get_dictvalue(context, context["key"])
    html = "<h3>" + context["key"] + "</h3>"
    logmessage("displaydict", "warning", selected_dick)
    for key, value in selected_dick.items():
        if type(value) not in [dict, list]:
            html += "<div class='w3-row'><div class='w3-col s4 w3-border'>"+key+"</div><div class='w3-col s8 w3-border'>"+value+"</div></div>"
    logmessage("displaydict", "warning", html)
    return html
