import logging
from PyWebSystem.PyUtil.TraceException import trace_exception


def logmessage(f_name="", m_type="", message=None, exception=None):
    logger = logging.getLogger(f_name)
    handler = logging.StreamHandler()
    format = logging.Formatter('%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
    if m_type == "warning":
        handler.setLevel(logging.WARNING)
        logger.propagate = 0
        logger.addHandler(handler)
        handler.setFormatter(format)
        logger.warning("%s,%s", message, trace_exception(exception, returnvalue=True))
        logger.removeHandler(handler)
    elif m_type == "error":
        handler.setLevel(logging.ERROR)
        logger.propagate = 0
        logger.addHandler(handler)
        handler.setFormatter(format)
        logger.error("%s,%s", message, trace_exception(exception, returnvalue=True))
    elif m_type == "debug":
        handler.setLevel(logging.DEBUG)
        logger.propagate = 0
        logger.addHandler(handler)
        handler.setFormatter(format)
        logger.debug("%s,%s", message, trace_exception(exception, returnvalue=True))
    else:
        handler.setLevel(logging.INFO)
        logger.propagate = 0
        logger.addHandler(handler)
        handler.setFormatter(format)
        logger.info("%s,%s", message, trace_exception(exception, returnvalue=True))
