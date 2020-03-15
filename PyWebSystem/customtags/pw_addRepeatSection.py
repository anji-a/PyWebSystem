from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.PyUtil.pw_extra_methods import id_generator
from django.template import Template
from PyWebSystem.PyUtil.DickUpdate import pw_loop
from PyWebSystem.customtags.pw_definePrimaryNode import definePrimaryNode
from PyWebSystem.HtmlParse.setElementPath import setElementPath


def addRepeatSection(context, *args, **kwargs):
    logmessage("addRepeatSection", "warning")
    backupPrimary = context["ElementPrimary"]
    primaryNode = context["ElementPrimary"]
    setElementPath(context)
    elepath = context.get("ElementPrimary", {}).get("elementpath", "")
    # logmessage("LayoutRepeat", "warning", elepath)
    Primary = definePrimaryNode(context, "", "", elepath)
    controlset = context.get("ElementPrimary", {}).get("controlset", {})
    generalset = controlset.get("generalset", {})
    gen_id = id_generator(10)
    repeathtml = "<div data-uitype='rowgroup' data-path='" + elepath + "' data-target=" + gen_id + " id=" + gen_id + ">"
    primaryNodeColumns = context["ElementPrimary"]["columns"]
    logmessage("addRepeatSection", "warning", context["Config"].get("ElementSettings", {}).get("Action", {}))
    logmessage("addRepeatSection", "warning", primaryNodeColumns)
    for index, key, path, value in pw_loop(Primary):
        if index == -1:
            pass
        else:
            value["elementpath"] = elepath + path
            repeathtml += "<div data-uitype='row' data-path='" + value["elementpath"] + "'>"
            for index, key, path, cvalue in pw_loop(primaryNodeColumns):
                bodyhtml = ""
                cvalue["elementpath"] = value["elementpath"]
                context["ElementPrimary"] = cvalue
                context["elpath"] = value["elementpath"]
                if cvalue.get("controltype", "") == "Layout":
                    # cvaluestr = json.dumps(cvalue)
                    html = '{%load TagUtility%} {%includeTag layout %}'
                elif cvalue.get("controltype", "") == "section":
                    html = '{%load TagUtility%}{%includeTag setpath as elpath1%} {%includeTag findelement as elementconfig%} {%with elpath=elpath1 ElementPrimary=elementconfig%} {%includeTag addsection %} {%endwith%}'
                t = Template(html)
                bodyhtml += t.render(context)
                repeathtml += bodyhtml
            repeathtml += "</div>"
            # logmessage("LayoutRepeat", "warning", repeathtml)
    footersection = generalset.get("footersection", "")
    footersectionhtml = ""
    if footersection != "" and footersection is not None:
        context["ElementPrimary"] = {"controlset": {}, "controltype": "section", "sectionname": footersection,
                                     "elementpath": elepath}
        context["elpath"] = elepath
        footerhtml = '{%load TagUtility%}{%includeTag setpath as elpath1%} {%includeTag findelement as elementconfig%} {%with elpath=elpath1 ElementPrimary=elementconfig%} {%includeTag addsection %} {%endwith%}'
        t = Template(footerhtml)
        footersectionhtml = t.render(context)
    repeathtml += footersectionhtml+"</div>"
    t = Template(repeathtml)
    html = t.render(context)
    #html = html + footersectionhtml
    context["ElementPrimary"] = backupPrimary
    return html
