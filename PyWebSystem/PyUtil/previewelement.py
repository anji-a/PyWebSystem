from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.customtags.pw_findelement import findelement
from PyWebSystem.PyUtil.RenderHtmlToString import render_html


def previewelement(context={}, action={}, *args, **kwargs):
    logmessage("previewelement", "warning", action)
    context["data_element"] = "dynamic"
    actiondate = action.get("actiondata", {})
    elementname = actiondate.get("refreshsection", "")
    if elementname == "":
        return ""
    else:
        # elementsource = findelement(context, ElementName=elementname)
        # logmessage("previewelement", "warning", elementsource)
        conf = {}
        conf["elements"] = [{"controltype": "section", 'sectionname': elementname}]  # it should be list
        # context.get("ElementPrimary", {})["sectionname"] = sectionname
        # config = json.dumps(conf)
        html = render_html(context, conf)
        logmessage("previewelement", "warning", html)
        context["element_html"] = context.get("element_html", "") + "openmodelwindow(event,\"" + html + "\" ,\"" + action.get("target", "") + "\")"
