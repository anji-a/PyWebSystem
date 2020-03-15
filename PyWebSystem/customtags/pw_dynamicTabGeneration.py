from django.template import Context, Template
from PyWebSystem.PyUtil.pw_logger import logmessage
import json
from PyWebSystem.PyUtil.pw_extra_methods import id_generator
from PyWebSystem.PyUtil.DickUpdate import pw_loop
from PyWebSystem.customtags.pw_definePrimaryNode import definePrimaryNode


def dynamicTabGeneration(context, *args, **kwargs):
    logmessage("dynamicTabGeneration", "warning", args)
    tabid = id_generator(6)
    conf = args[2]
    conf = conf[1:]
    conf = conf[:-1]
    confdict = json.loads(conf)
    if confdict.get("TabNode", "")[0] == ".":
        elepath = confdict.get("elementpath", "") + confdict.get("TabNode", "")
    else:
        elepath = confdict.get("TabNode", "")
    haderhtml = '<div data-target="tablinks" class="w3-bar w3-black">'
    contenthtml = '<div data-target="tabcontent" class="w3-container w3-border">'
    tablink = ""
    tabcontent = ""
    Primary = definePrimaryNode(context, "", "", elepath)
    # this code for Dict, need to simplify for list also
    for index, key, path, value in pw_loop(Primary):
        i = 0
        gen_id = id_generator(6)
        value["elementpath"] = elepath+path
        if i == "1":
            tablink += '<button class="w3-bar-item w3-button tablink active" data-tabid="'+tabid+'" data-type="TabLink" data-node="' + value.get(
                'elementpath', "") + '" data-target="' + gen_id + '" onclick="w3tabclick(event)">' + value.get(
                confdict.get('TabName', ''), '') + '</button>'
            tabcontent += '<div data-target="' + gen_id + '" data-type="TabData" data-tabid="'+tabid+'" class="nodisplay display">'
        else:
            tablink += '<button class="w3-bar-item w3-button tablink" data-tabid="'+tabid+'" data-type="TabLink" data-node="'+value.get('elementpath', "")+'" data-target="'+gen_id+'" onclick="w3tabclick(event)">'+ value.get(confdict.get('TabName', '') , '')+'</button>'
            tabcontent += '<div data-target="' + gen_id + '" data-type="TabData" data-tabid="'+tabid+'" class="nodisplay">'
        i += 1
        for key, cvalue in enumerate(confdict.get("columns")):
            bodyhtml = ""
            """if cvalue.get("PrimaryNode", "") == "":
                cvalue["elementpath"] = value.get("elementpath", "")
            elif cvalue.get("PrimaryNode", "")[0] == ".":
                cvalue["elementpath"] = cvalue.get("PrimaryNode", "")
            else:
                cvalue["elementpath"] = value.get("elementpath", "") + cvalue.get("PrimaryNode", "")"""
            cvalue["elementpath"] = cvalue["elementpath"]
            context["ElementPrimary"] = cvalue
            context["elpath"] = cvalue["elementpath"]
            if cvalue.get("controltype", "") == "Layout":
                #cvaluestr = json.dumps(cvalue)
                html = '{%load TagUtility%} {%includeTag layout %}'
            elif cvalue.get("controltype", "") == "LayoutRepeat":
                #cvaluestr = json.dumps(cvalue)
                html = '{%load TagUtility%} {%includeTag LayoutRepeat %}'
            elif cvalue.get("controltype", "") == "TabGroup":
                html = "{%load TagUtility%} {%includeTag tab %}"
            t = Template(html)
            bodyhtml += t.render(context)
            tabcontent += bodyhtml + '</div>'
    haderhtml += tablink + "</div>"
    contenthtml += tabcontent + "</div>"
    # Do second time render to get context values
    t = Template(haderhtml+contenthtml)
    html = t.render(context)
    return html
