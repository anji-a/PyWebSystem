from PyWebSystem.PyUtil.pw_logger import logmessage
import json
from PyWebSystem.PyUtil.RenderHtmlToString import render_html


def opensettings(context={}, action={}, *args, **kwargs):
    logmessage("opensettings", "warning", action)
    logmessage("opensettings", "warning", context.get("Config", {}).get("ElementSettings", {}))
    context.get("Config", {})["ElementSettings"] = json.loads(action.get("actiondata", {}).get('config', '{}'))
    context.get("Config", {})["ElementSettings"]["id"] = action.get("actiondata", {}).get('id', '')
    context.get("Config", {})["ElementSettings"]["elementType"] = action.get("actiondata", {}).get('elementType', '')
    conf = {}
    conf["elements"] = [{"controltype": "section", 'sectionname': "LayoutSettings"}]  # it should be list
    # context.get("ElementPrimary", {})["sectionname"] = sectionname
    # config = json.dumps(conf)
    html = render_html(context, conf)
    logmessage("previewelement", "warning", html)
    context["element_html"] = context.get("element_html", "") + "openmodelwindow(event,\"" + html + "\" ,\"" + action.get("target", "") + "\");"
