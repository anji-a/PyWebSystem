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
    logmessage(__name__, "warning", var)
    return [{"a": "a"}]
