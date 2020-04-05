from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.PyUtil.RenderHtmlToString import render_html


def refreshsection(context={}, action={}, *args, **kwargs):
    logmessage("refreshsection", "warning", action)
    context["data_element"] = "dynamic"
    # eventdata = context.get("Config", {}).get("EventData", {}).get("data-controlset", {}).get("actiondata", {})
    eventdata = action.get("actiondata", {})
    sectionname = eventdata.get("refreshsection", "")
    logmessage("refreshsection", "warning", eventdata)
    html = "{% load TagUtility %}"
    if sectionname != "":
        refreshsectionwrapper(context, eventdata.get("refreshnode", ""), sectionname, eventdata.get("refreshid", ""))
        """context["elpath"] = eventdata.get("refreshnode", "")
        conf = {}
        conf["elements"] = [{"controltype": "section", 'sectionname': sectionname}]  # it should be list
        # context.get("ElementPrimary", {})["sectionname"] = sectionname
        # config = json.dumps(conf)
        html = render_html(context, conf)
        logmessage("refreshsection", "warning", context["elpath"])
        # html += '{%includeTag ParseConfigToHtml \'' + config + '\'%}'
        # t = Template(html)
        # c = Context(context)
        # html = t.render(c)
        #logmessage("refreshsection", "warning", html)
        html = "pw(event).refreshsection(\""+eventdata.get("refreshid", "")+"\",\""+html+"\")"
        context["element_html"] = html"""



def refreshsectionwrapper(context, elpath, sectionname, elementid):
    context["elpath"] = elpath
    conf = {}
    conf["elements"] = [{"controltype": "section", 'sectionname': sectionname}]  # it should be list
    # context.get("ElementPrimary", {})["sectionname"] = sectionname
    # config = json.dumps(conf)
    html = render_html(context, conf)
    logmessage("refreshsection", "warning", context["elpath"])
    # html += '{%includeTag ParseConfigToHtml \'' + config + '\'%}'
    # t = Template(html)
    # c = Context(context)
    # html = t.render(c)
    # logmessage("refreshsection", "warning", html)
    html = "pw(event).refreshsection(\"" + elementid + "\",\"" + html + "\")"
    context["element_html"] = context.get("element_html", "") + html
