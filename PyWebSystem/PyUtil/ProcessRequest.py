from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import HttpResponse
from json import dumps
from time import sleep
from django.shortcuts import render
from django.core.cache import cache
from django.contrib.sessions.backends.db import SessionStore
from PyWebSystem.PyUtil.GetSessionObject import get_session, update_session, update_request
from PyWebSystem.PyUtil.DickUpdate import dick_update, process_request_dick
from PyWebSystem.PyUtil.ProcessEventData import process_event
from PyWebSystem.db.dbtransaction import Transaction
from PyWebSystem.PyUtil.pw_logger import logmessage


@csrf_exempt
def process_request(request):
    _transaction_ = Transaction()
    session = get_session(request.session.session_key)
    # /////////logic starts here /////////////
    params = {"Etype": "Params", "Session": session}
    context = update_request(request, session, params=params)
    context["_transaction_"] = _transaction_
    logmessage("process_request", "warning", context.get("_transaction_", ""))
    # print(params)
    print("....................")
    process_event(context, params=params)

    # //////////Logic Ends here //////////////
    # resdata = {"html": render_to_string('PyWeb/pw_screen_render.html', context), 'responseData': context}
    resdata = {"html": context.get("element_html", ""), 'responseData': context}
    # print(context, "\n..................")
    # /////////Reset the HTML Element /////////
    context["element_html"] = ""
    update_session(session)
    _transaction_.close_transaction()
    # return JsonResponse(resdata)
    return HttpResponse(dumps(resdata), content_type='application/json')
