from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.PyUtil.pw_extra_methods import id_generator
from django.template import Template


def generatetab(context, *args, **kwargs):
    logmessage("generatetab", "warning")
    backupPrimary = context["Primary"]
    primaryNode = context["Primary"]["columns"]
    haderhtml = '<div data-target="tablinks" class="w3-bar w3-black">'
    contenthtml = '<div data-target="tabcontent" class="w3-container w3-border">'
    tablink = ""
    tabcontent = ""
    for key, value in enumerate(primaryNode):
        gen_id = id_generator(6)
        tablink += '<button class="w3-bar-item w3-button tablink" data-target="'+gen_id+'" onclick="w3tabclick(event)">'+ value.get('TabName', '')+'</button>'
        for key, value in enumerate(value.get("columns", [])):
            bodyhtml = ""
            if value.get("controltype", "") == "Layout":
                context["Primary"] = value
                html = "{%load TagUtility%} {%includeTag layout %} "
                t = Template(html)
                bodyhtml += t.render(context)
        #tabcontent += contenthtml+'{% with Config=Config.config Primary=Primary worknodes=worknodes %} {%includeTag layout %}  {% endwith %}'+"</div>"
        tabcontent += bodyhtml+'</div>'
    context["Primary"] = backupPrimary
    haderhtml += tablink + "</div>"
    #contenthtml += tabcontent + "</div>"
    return haderhtml+tabcontent
