import json, sys
from PyWebSystem.PyUtil.pw_logger import logmessage


def parsedicttohtml(souurcedt={}):
    #print(souurcedt)
    html = "{% load TagUtility %}"
    elelist = souurcedt.get("elements", [])
    for key, ele in enumerate(elelist):
        #config = json.dumps(ele.get("controlset", {}))
        #columns = json.dumps(ele.get("columns", []))
        # should send configuration between ""
        try:
            config = json.dumps(ele)
            logmessage(__name__, "warning", message=config)
            html += '{%includeTag layout \'' + config + '\'%}'

        except Exception as e:
            logmessage(__name__, "error", exception=sys.exc_info())
        # html += "{%includeTag layout \""+config+"\" \""+columns+"\"%}"
    #print(html)
    return html
