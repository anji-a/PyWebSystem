from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import HttpResponse
from json import dumps
from time import sleep
from django.shortcuts import render


@csrf_exempt
def process_request(request):
    #sleep(3)
    my_dic = request.POST.dict()
    print(request.session)
    resdata = {"html": render_to_string('PyWeb/pw_screen_render.html', my_dic), 'responseData': my_dic}
    # return JsonResponse(resdata)
    return HttpResponse(dumps(resdata), content_type='application/json')
