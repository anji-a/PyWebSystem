from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.PyUtil.pw_extra_methods import id_generator
from django.template import Template
import json


def generatetab(context, *args, **kwargs):
    logmessage("generatetab", "warning")
    backupPrimary = context["ElementPrimary"]
    primaryNode = context["ElementPrimary"]["columns"]

    if backupPrimary.get("TabType", "") == "Dynamic":
        html = dynamicTabGeneration(context, primaryNode, backupPrimary)
    else:
        html = staticTabGenearation(context, primaryNode, backupPrimary)
    context["ElementPrimary"] = backupPrimary
    return html


def dynamicTabGeneration(context, colums, backupPrimary):
    logmessage("generatetab-->dynamicTabGeneration", "warning", backupPrimary)
    tabconf = json.dumps(backupPrimary)
    html = "{%load TagUtility%}{%includeTag dynamicTabGeneration '"+tabconf+"'%}"
    t = Template(html)
    html = t.render(context)
    return html


def staticTabGenearation(context, columns, backupPrimary):
    logmessage("staticTabGenearation", "warning")
    tabid = id_generator(6)
    haderhtml = '<div data-target="tablinks" class="w3-bar w3-black">'
    contenthtml = '<div data-target="tabcontent" class="w3-container w3-border">'
    tablink = ""
    tabcontent = ""
    for key, value in enumerate(columns):
        controlset = value.get("controlset", {})
        generalset = controlset.get("generalset", {})
        gen_id = id_generator(6)
        if value.get("PrimaryNode", "") == "":
            value["elementpath"] = backupPrimary.get("elementpath", "")
        else:
            value["elementpath"] = backupPrimary.get("elementpath", "") + value.get("PrimaryNode", "")
        if generalset.get("Active", "") == "true":
            tablink += '<button class="w3-bar-item w3-button tablink active" data-tabid="'+tabid+'" data-type="TabLink" data-node="' + value.get(
                'elementpath', "") + '" data-target="' + gen_id + '" onclick="w3tabclick(event)">' + generalset.get(
                'TitleValue', '') + '</button>'
            tabcontent += '<div data-target="' + gen_id + '" data-type="TabData" data-tabid="'+tabid+'" class="nodisplay display">'
        else:
            tablink += '<button class="w3-bar-item w3-button tablink" data-type="TabLink" data-tabid="'+tabid+'" data-node="'+value.get('elementpath', "")+'" data-target="'+gen_id+'" onclick="w3tabclick(event)">'+ generalset.get('TitleValue', '')+'</button>'
            tabcontent += '<div data-target="' + gen_id + '" data-type="TabData" data-tabid="'+tabid+'" class="nodisplay">'
        bodyhtml = ""
        context["ElementPrimary"] = value
        html = "{%load TagUtility%}{%includeTag setpath as elpath1%} {%includeTag findelement as elementconfig%} {%with elpath=elpath1 ElementPrimary=elementconfig%} {%includeTag addsection %} {%endwith%}"
        logmessage("staticTabGenearation", "warning", html)
        t = Template(html)
        bodyhtml += t.render(context)
        # Below for loop code not required based on requirement delete it later
        for key, cvalue in enumerate(value.get("columns", [])):
            """if cvalue.get("PrimaryNode", "") == "":
                cvalue["elementpath"] = value.get("elementpath", "")
            else:
                cvalue["elementpath"] = value.get("elementpath", "") + cvalue.get("PrimaryNode", "")"""
            cvalue["elementpath"] = value["elementpath"]
            context["ElementPrimary"] = cvalue
            context["elpath"] = value["elementpath"]
            logmessage("staticTabGenearation", "warning", value["elementpath"])
            if cvalue.get("controltype", "") == "Layout":
                html = "{%load TagUtility%} {%includeTag layout %}"
            elif cvalue.get("controltype", "") == "TabGroup":
                html = "{%load TagUtility%} {%includeTag tab %}"
            elif cvalue.get("controltype", "") == "LayoutRepeat":
                html = "{%load TagUtility%} {%includeTag LayoutRepeat %}"
            elif cvalue.get("controltype", "") == "section":
                html = "{%load TagUtility%}{%includeTag setpath as elpath1%} {%includeTag findelement as elementconfig%} {%with elpath=elpath1 ElementPrimary=elementconfig%} {%includeTag addsection %} {%endwith%}"
            logmessage("staticTabGenearation", "warning", html)
            t = Template(html)
            bodyhtml += t.render(context)
        tabcontent += bodyhtml + '</div>'
        #tabcontent += contenthtml+'{% with Config=Config.config Primary=Primary worknodes=worknodes %} {%includeTag layout %}  {% endwith %}'+"</div>"
    haderhtml += tablink + "</div>"
    contenthtml += tabcontent + "</div>"
    return haderhtml+contenthtml
