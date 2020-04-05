from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.PyUtil.RenderHtmlToString import render_html
from PyWebSystem.PyUtil.pw_extra_methods import createElementNode
import PyWebSystem.PyConfig.GlobalValues as GV


def OpenNewUIElement(context={}, action={}, *args, **kwargs):
    logmessage("OpenNewUIElement", "warning", action)
    _transaction_ = context["_transaction_"]  # copy transaction to variable
    del context["_transaction_"]  # delete transaction from Old context
    Node = "NewElement"
    NodePrimary = "Standard"
    GV.context = createElementNode(GV.session, Node, NodePrimary)
    GV.context["_transaction_"] = _transaction_
    conf = {}
    conf["elements"] = [{"controltype": "html", 'sectionname': "NewUIEditor"}]  # it should be list
    logmessage("OpenNewUIElement", "warning", GV.context)
    html = render_html(GV.context, conf)
    html = "<div data-find='worknode' data-primary="+NodePrimary+" data-node="+GV.context.get("NodeID", "")+">"+html+"</div>"
    context["element_html"] = context.get("element_html", "") + "w3openworktab(event,\""+"New"+"\",\"" + html + "\")"

