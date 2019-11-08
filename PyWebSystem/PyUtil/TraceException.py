import traceback


def trace_exception(error, returnvalue=False):
    if returnvalue:
        if error is not None:
            exc_type, exc_value, exc_traceback = error
            return (repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
        else:
            return ""
    else:
        if error is not None:
            exc_type, exc_value, exc_traceback = error
            print(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
        else:
            print("")
