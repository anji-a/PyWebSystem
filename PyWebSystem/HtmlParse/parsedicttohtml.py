import json, sys
from PyWebSystem.PyUtil.pw_logger import logmessage
from django.template import Template, Context


def parsedicttohtml(souurcedt={}):
    logmessage(__name__, "warning", message=souurcedt)
    html = "{% load TagUtility %}"
    elelist = souurcedt.get("elements", [])
    """
    for key, ele in enumerate(elelist):
        #config = json.dumps(ele.get("controlset", {}))
        #columns = json.dumps(ele.get("columns", []))
        # should send configuration between ""
        try:
            config = json.dumps(ele)
            logmessage(__name__, "warning", message=config)
            # html += '{%includeTag layout \'' + config + '\'%}'
            html += '{%includeTag ParseConfigToHtml \'' + config + '\'%}'

        except Exception as e:
            logmessage(__name__, "error", exception=sys.exc_info())
        # html += "{%includeTag layout \""+config+"\" \""+columns+"\"%}"
    #print(html)"""
    config = json.dumps(elelist)
    html += '{%includeTag ParseConfigToHtml \'' + config + '\'%}'
    t = Template(html)
    c = Context({})
    html = t.render(c)

    return html
