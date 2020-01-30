import sys

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from PyWebSystem.PyUtil.GetSessionObject import get_session, update_session
from django.core.cache import cache
from django.core.cache import caches
from PyWebSystem.PyUtil.pw_extra_methods import createNode
from PyWebSystem.PyUtil.pw_logger import logmessage


def index(request):
    return render(request, 'PyWeb/login.html', context={})


@csrf_exempt
def login_app(request):
    logmessage("login_app", "warning")
    if request.method == 'POST' or request.method == 'GET':
        try:
            username = request.POST['username']
            password = request.POST['psw']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                OperatorID = {"userid": username, "loginTime": str(datetime.now()), "portal_type": "Developer"}
                StandardNode = "Standard"
                Requester = {"sessionid": request.session.session_key, "userid": username, "loginTime": str(datetime.now())}
                session = get_session(request.session.session_key)
                session["OperatorID"] = OperatorID
                session["Requester"] = Requester
                createNode(session, StandardNode)
                update_session(session)
                #print(session, "\n....................")
                logmessage("login_app", "warning", session)
                # return render(request, 'PyWeb/workspace.html', context=session) used to check for old code
                return render(request, 'PyWeb/py_editor.html', context=session)
            else:
                return render(request, 'PyWeb/login.html',
                              context={'login_message': "Login not success Please try to re login"})
        except Exception:
            logmessage("login_app", "error", exception=sys.exc_info())
    else:
        print("its get method")


def logout_app(request):
    """
    Used to log out the user
    :param request:
    :return:
    """
    try:
        session = get_session(request.session.session_key)
        del session
        logout(request)
        return render(request, 'PyWeb/login.html', context={'loginmessage': "Successfully logged out, Please login here"})
    except:
        print(sys.exc_info())
