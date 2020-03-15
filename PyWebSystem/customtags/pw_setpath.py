from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.HtmlParse.setElementPath import setElementPath


def setpath(context, *args, **kwargs):
    logmessage("setpath", "warning", context["ElementPrimary"])
    setElementPath(context)
    path = context["ElementPrimary"]["elementpath"]
    logmessage("setpath", "warning", path)
    return path
