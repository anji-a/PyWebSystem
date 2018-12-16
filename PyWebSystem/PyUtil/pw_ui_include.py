from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def pw_ui_include(request):
    my_dic = request.POST.dict()
    return render(request, 'PyWeb/pw_screen_render.html', context=my_dic)
