from PyWebSystem.PyUtil.RenderHtmlToString import render_html


def model_window(context={}, action={}, *args, **kwargs):
    context["element"] = action.get("form", "")
    context["data_element"] = "static"
    html = render_html(context)
    if context.get("element_html", "") == "":
        context["element_html"] = "$('#"+action.get("target", "")+"Body').html(\"" + html + "\");$('#"+action.get('target', '')+"').modal({'show':true,backdrop:'static'});"
    else:
        context["element_html"] += "$('#"+action.get("target", "")+"Body').html(\"" + html + "\");$('#"+action.get('target', '')+"').modal({'show':true,backdrop:'static'});"


def model_close(context={}, action={}, *args, **kwargs):
    html = "var location=$(event.target).closest(\"[role='dialog']\").attr(\"id\");"
    html += "closemodal(location);"
    #print(html)
    if context.get("element_html", "") == "":
        context["element_html"] = html
    else:
        context["element_html"] += html


def landing_tab(context={}, action={}, *args, **kwargs):
    #addTabByHtmlLocationName(html,location,tabname)
    session = kwargs.get("params", {}).get("Session", {})
    threadName = action.get("purpose", "")
    standardthread = context.get("standard", {})
    html = ""
    if threadName is not "":
        standard = {"element": standardthread.get("element", ""), "element_type": standardthread.get("element_type", ""), "dir": standardthread.get("dir", "")}
        session[threadName] = {}
        session[threadName]["standard"] = standard.copy()
        session[threadName]["EventData"] = context.get("EventData", {}).copy()
        threadcontext = session[threadName]
        threadcontext["element"] = action.get("purpose", "")
        threadcontext["data_element"] = "static"
        html = render_html(threadcontext)

    html = "addTabByHtmlLocationName(\"" + html + "\",'workTabs',\""+threadName+"\")"
    if context.get("element_html", "") == "":
        context["element_html"] = html
    else:
        context["element_html"] += html
