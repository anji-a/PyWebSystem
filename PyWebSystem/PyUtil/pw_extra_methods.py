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
        session["NodeName"] = NodeName
        session[portalid] = {}
        session[portalid]["portalid"] = portalid
        session[portalid]["PortalName"] = "StandardNode"
        session[portalid]["NodeName"] = NodeName
        session[portalid][NodeName] = {}
        session[portalid]["OperatorID"] = session["OperatorID"]
        session[portalid]["Requester"] = session["Requester"]
    except Exception:
        logmessage("createNode", "error", exception=sys.exc_info())

