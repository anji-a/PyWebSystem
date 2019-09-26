import traceback


def trace_exception(error):
    exc_type, exc_value, exc_traceback = error
    print(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))

