from PyWebSystem.PyUtil.pw_extra_methods import id_generator
from PyWebSystem.PyUtil.pw_logger import logmessage


def assignid(context, *args, **kwargs):
    logmessage("assignid", "warning")
    return id_generator(6)
