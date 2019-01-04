from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from PyWebSystem.PyUtil.GetSessionObject import update_request, get_session, update_session
from PyWebSystem.PyUtil.ProcessEventData import process_event
from django.http import HttpResponse
from json import dumps

from bs4 import BeautifulSoup


@csrf_exempt
def pw_ui_include(request):
    session = get_session(request.session.session_key)
    # /////////logic starts here /////////////
    params = {"Etype": "Params"}
    context = update_request(request, session, params=params)
    #print(params)
    process_event(context, params=params)

    # //////////Logic Ends here //////////////

    #resdata = {"html": render_to_string('PyWeb/pw_screen_render.html', context), 'responseData': context}
    resdata = {"html": context.get("element_html", ""), 'responseData': context}
    #print(context, "\n..................")
    # /////////Reset the HTML Element /////////
    context["element_html"] = ""
    update_session(session)
    return HttpResponse(dumps(resdata), content_type='application/json')
    #return render(request, 'PyWeb/pw_screen_render.html', context=context)
