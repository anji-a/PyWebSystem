from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.PyUtil.DickUpdate import get_val, getkeylist


def GetElementPath(context, *args, **kwargs):
    logmessage("GetElementPath", "warning", args)
    result = ""
    for key, value in enumerate(args):
        logmessage("GetElementPath", "warning", value)
        if key in [0, 1]:
            pass
        elif key == 2 and value != "as":
            keylistfinal = getkeylist(value)
            logmessage("GetElementPath", "warning", keylistfinal)
            if result == "":
                result = get_val(context, keylistfinal)
                logmessage("GetElementPath", "warning", result)
            else:
                result += "."+get_val(context, keylistfinal)
                logmessage("GetElementPath", "warning", result)
        elif value == "as":
            logmessage("GetElementPath", "warning", result)
            return result

