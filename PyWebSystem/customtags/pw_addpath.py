from PyWebSystem.PyUtil.pw_logger import logmessage


def addpath(value, path):
    logmessage("addpath", "warning", [value, path])
    if path is None or value == "" or value is None:
        return ""
    elif value[0] != ".":
        return value
    else:
        return path+'%s' % value
