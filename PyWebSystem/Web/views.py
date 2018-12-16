import sys

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'PyWeb/login.html', context={})


@csrf_exempt
def login_app(request):
    if request.method == 'POST' or request.method == 'GET':
        try:
            username = request.POST['username']
            password = request.POST['psw']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'PyWeb/workspace.html', context={'user': user})

            else:
                return render(request, 'PyWeb/login.html',
                              context={'login_message': "Login not success Please try to re login"})
        except:
            print(sys.exc_info())
    else:
        print("its get method")


def logout_app(request):
    """
    Used to log out the user
    :param request:
    :return:
    """
    try:
        logout(request)
        return render(request, 'PyWeb/login.html', context={'loginmessage': "Successfully logged out, Please login here"})
    except:
        print(sys.exc_info())
