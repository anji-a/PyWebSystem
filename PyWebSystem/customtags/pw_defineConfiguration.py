from PyWebSystem.PyUtil.pw_logger import logmessage


def defineConfiguration(context, *args, **kwargs):
    var = {}
    for k, value in enumerate(args[2].split(".")):
        if k == 0:
            var = context.get(value, {})
        elif var.keys():
            var = var.get(value, {})
        else:
            pass
    logmessage("defineConfiguration", "warning", var)
    return var


def defineConfigurationwithkey(context, key):
    var = {}
    for k, value in enumerate(key.split(".")):
        if k == 0:
            var = context.get(value, {})
        elif var.keys():
            var = var.get(value, {})
        else:
            pass
    logmessage("defineConfigurationwithkey", "warning", var)
    return var
