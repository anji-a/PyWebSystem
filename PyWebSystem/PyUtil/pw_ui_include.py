from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from PyWebSystem.PyUtil.GetSessionObject import update_request, get_session, update_session
from PyWebSystem.PyUtil.ProcessEventData import process_event
from django.http import HttpResponse
from json import dumps
from PyWebSystem.db.dbtransaction import Transaction
from PyWebSystem.PyUtil.pw_logger import logmessage
import PyWebSystem.PyConfig.GlobalValues as GV


@csrf_exempt
def pw_ui_include(request, *args, **kwargs):
    GV.init()
    callfrom = kwargs.get("callingFrom", "")
    _transaction_ = Transaction()
    logmessage(__name__, "warning")
    session = get_session(request.session.session_key)
    GV.session = session
    # print(session)
    params = {"Etype": "Params"}
    context = update_request(request, session, params=params)
    context["_transaction_"] = _transaction_
    GV.context = context
    process_event(GV.context, params=params)
    # resdata = {"html": render_to_string('PyWeb/pw_screen_render.html', context), 'responseData': context}
    if callfrom == "login_app":  # need to change this logic later
        html = render(request, 'PyWeb/py_editor.html', context=GV.context)
        # resdata = {"html": html, 'responseData': context}
        del _transaction_
        del GV.context["_transaction_"]
        update_session(session)
        return html
    else:
        resdata = {"html": context.get("element_html", ""), 'responseData': GV.context}
    context["element_html"] = ""
    _transaction_.close_transaction()
    del _transaction_
    del GV.context["_transaction_"]
    update_session(GV.session)
    return HttpResponse(dumps(resdata), content_type='application/json')
    #return render(request, 'PyWeb/pw_screen_render.html', context=context)
