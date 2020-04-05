import string
import random
from PyWebSystem.PyUtil.pw_logger import logmessage
import sys


def id_generator(size=6, prefix="", suffix="", chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    logmessage("id_generator", "warning")
    genstring = ''.join(random.choice(chars) for _ in range(size))
    return prefix+genstring+suffix


def createNode(session, NodeName):
    logmessage("createNode", "warning")
    try:
        portalid = id_generator(20)
        session["portalid"] = portalid
        # session["NodeName"] = "Portal"
        session[portalid] = {}
        session[portalid]["NodeID"] = portalid
        session[portalid]["NodeName"] = "Portal"
        session[portalid]["PrimaryNode"] = NodeName
        session[portalid][NodeName] = {}
        session[portalid]["OperatorID"] = session["OperatorID"]
        session[portalid]["Requester"] = session["Requester"]
    except Exception:
        logmessage("createNode", "error", exception=sys.exc_info())


def createElementNode(session, nodename, primarynode):
    logmessage("createElementNode", "warning")
    try:
        NodeID = id_generator(20)
        portalid = session["portalid"]
        session[NodeID] = {}
        session[NodeID]["NodeID"] = NodeID
        session[NodeID]["NodeName"] = nodename
        session[NodeID]["PrimaryNode"] = primarynode
        session[NodeID][primarynode] = {}
        session[NodeID]["OperatorID"] = session["OperatorID"]
        session[NodeID]["Requester"] = session["Requester"]
        session[NodeID]["Portal"] = session[portalid]
        return session[NodeID]
    except Exception:
        logmessage("createElementNode", "error", exception=sys.exc_info())


def closeoldcontext(context):
    del context["_transaction_"]
