from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from PyWebSystem.PyUtil.GetSessionObject import update_request, get_session, update_session
from PyWebSystem.PyUtil.ProcessEventData import process_event
from django.http import HttpResponse
from json import dumps
from PyWebSystem.db.dbtransaction import Transaction
from PyWebSystem.PyUtil.pw_logger import logmessage


@csrf_exempt
def pw_ui_include(request):
    _transaction_ = Transaction()
    logmessage(__name__, "warning")
    session = get_session(request.session.session_key)
    # /////////logic starts here /////////////
    params = {"Etype": "Params"}
    context = update_request(request, session, params=params)
    #print(params)
    context["_transaction_"] = _transaction_
    process_event(context, params=params)

    # //////////Logic Ends here //////////////

    #resdata = {"html": render_to_string('PyWeb/pw_screen_render.html', context), 'responseData': context}
    resdata = {"html": context.get("element_html", ""), 'responseData': context}
    #print(context, "\n..................")
    # /////////Reset the HTML Element /////////
    context["element_html"] = ""
    _transaction_.close_transaction()
    del _transaction_
    del context["_transaction_"]
    update_session(session)
    return HttpResponse(dumps(resdata), content_type='application/json')
    #return render(request, 'PyWeb/pw_screen_render.html', context=context)
