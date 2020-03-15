from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.PyUtil.pw_extra_methods import id_generator
from django.template import Template
from PyWebSystem.PyUtil.DickUpdate import pw_loop
from PyWebSystem.customtags.pw_definePrimaryNode import definePrimaryNode


def LayoutRepeat(context, *args, **kwargs):
    logmessage("LayoutRepeat", "warning")
    backupPrimary = context["ElementPrimary"]
    primaryNode = context["ElementPrimary"]
    # logmessage("LayoutRepeat", "warning", primaryNode.get("elementpath", ""))
    if primaryNode.get("PrimaryNode", "")[0] == ".":
        elepath = primaryNode.get("elementpath", "") + primaryNode.get("PrimaryNode", "")
    else:
        elepath = primaryNode.get("PrimaryNode", "")
    # logmessage("LayoutRepeat", "warning", elepath)
    Primary = definePrimaryNode(context, "", "", elepath)
    # logmessage("LayoutRepeat", "warning", Primary)
    gen_id = id_generator(10)
    repeathtml = "<div data-uitype='rowgroup' data-path='"+elepath+"' data-target=" + gen_id + " id="+gen_id+">"
    primaryNodeColumns = context["ElementPrimary"]["columns"]
    addrowicon = context["ElementPrimary"].get("addrowlay", {})
    logmessage("LayoutRepeat", "warning", primaryNodeColumns)
    if addrowicon.get("controltype", "") == "Layout":
        addrowicon["elementpath"] = elepath
        context["ElementPrimary"] = addrowicon
        context["elpath"] = addrowicon["elementpath"]
        html = '{%load TagUtility%} {%includeTag layout %}'
        t = Template(html)
        rowhtml = t.render(context)
    for index, key, path, value in pw_loop(Primary):
        if index == -1:
            pass
        else:
            value["elementpath"] = elepath + path
            repeathtml += "<div data-uitype='row' data-path='" + value["elementpath"] + "'>"
            for index, key, path, cvalue in pw_loop(primaryNodeColumns):
                bodyhtml = ""
                """if cvalue.get("PrimaryNode", "") == "":
                    cvalue["elementpath"] = value.get("elementpath", "")
                elif cvalue.get("PrimaryNode", "")[0] == ".":
                    cvalue["elementpath"] = cvalue.get("PrimaryNode", "")
                else:
                    cvalue["elementpath"] = value.get("elementpath", "") + cvalue.get("PrimaryNode", "")"""
                cvalue["elementpath"] = value["elementpath"]
                context["ElementPrimary"] = cvalue
                context["elpath"] = value["elementpath"]
                if cvalue.get("controltype", "") == "Layout":
                    # cvaluestr = json.dumps(cvalue)
                    html = '{%load TagUtility%} {%includeTag layout %}'
                elif cvalue.get("controltype", "") == "section":
                    html = '{%load TagUtility%} {%includeTag findelement as elementconfig%}{%with elpath=ElementPrimary.elementpath ElementPrimary=elementconfig%}{%includeTag addsection %}{%endwith%}'
                t = Template(html)
                bodyhtml += t.render(context)
                repeathtml += bodyhtml
            repeathtml += "</div>"
                # logmessage("LayoutRepeat", "warning", repeathtml)
    repeathtml += rowhtml+"</div>"
    t = Template(repeathtml)
    html = t.render(context)
    context["ElementPrimary"] = backupPrimary
    return html
