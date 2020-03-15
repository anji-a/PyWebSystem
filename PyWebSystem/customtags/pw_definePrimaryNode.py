from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.PyUtil.DickUpdate import get_val, getkeylist


def definePrimaryNode(context, *args, **kwargs):
    logmessage("definePrimaryNode", "warning", args)
    """keylist = args[2].split(".")
    keylistfinal = []
    for key, value in enumerate(keylist):
       if value[value.__len__() - 1] == "]":
            value = value[:-1]
            value.replace("]", '')
            valuelist = value.split('[')
            for key, value in enumerate(valuelist):
                if key == 0:
                    keylistfinal.append(value)
                else:
                    keylistfinal.append(int(value))
       else:
           keylistfinal.append(value)"""
    keylistfinal = getkeylist(args[2])
    var = get_val(context, keylistfinal)
    logmessage("definePrimaryNode", "warning", var)
    """if var is None or var is "":
        key = context.get("root_node", "Standard").split(".")
        logmessage("definePrimaryNode", "warning", key)
        var = get_val(context, key)
    # else:
        # var = get_val(context, var)"""
    # logmessage("definePrimaryNode", "warning", var)
    return var

