from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from PyWebSystem.PyUtil.GetSessionObject import get_session, update_session
from PyWebSystem.PyUtil.DickUpdate import process_request_dick, key_list, get_val
import json
from django.template.loader import render_to_string
from PyWebSystem.PyUtil.RenderHtmlToString import render_html
from bs4 import BeautifulSoup


@csrf_exempt
def memory_check(request):
    my_dic = request.POST.dict()
    print(my_dic)
    data_controlset = json.loads(my_dic.get("data-controlset", '{}'))
    session = get_session(request.session.session_key)
    root_obj = session.get(my_dic.get("root_data", ""), {})
    #process_request_dick(my_dic, root_obj)
    #update_session(session)
    keylist = key_list(data_controlset.get("select_dict", "$DOperatorID"))
    print(keylist, "\n.................................")
    selected_dick = get_val(session, keylist)
    selected_dick["select_dict"] = keylist[-1]
    selected_dick["root_data"] = my_dic.get("root_data", "")
        #{"select_dict": session.get("Development", "").get("select_dict", "")}
    #selected_dick.update(session.get(session.get("Development", "").get("select_dict", ""), {}).copy())
    session["selected_dick"] = selected_dick
    print(session)
    return render(request, 'PyWeb/pw_memory.html', context={"context": session})


def memory_verification(context={}, action={}, *args, **kwargs):
    params = kwargs.get("params", {})
    context["element"] = action.get("purpose", "")
    context["data_element"] = "static"
    session = get_session(params.get("sessionid", ""))
    keylist = key_list(action.get("select_dict", "$DOperatorID"))
    print(keylist)
    selected_dick = get_val(session, keylist)
    session["selected_dick"] = selected_dick
    selected_dick["select_dict"] = keylist[-1]
    #html = render_html(session)
    html = render_to_string('PyWeb/pw_memory.html', context={"context": session})
    #window.open("https://www.w3schools.com", "_blank", "toolbar=yes,scrollbars=yes,resizable=yes,top=500,left=500,width=400,height=400");
    soup = BeautifulSoup(html, 'html.parser')
    html = soup.find(id=action.get("target", "pw_memory_window"))
    html = str(html)
    #print(html)
    print(session)
    html = "".join([line.strip("\n\t") for line in html])
    html = html.replace('"', '\\"')
    html = html.replace("/*", "\\/*")
    html = html.replace("*/", "*\\/")
    if context.get("element_html", "") == "":
        if action.get("select_dict", "$DOperatorID") == "$DOperatorID":
            context["element_html"] = "var memorywindow = window.open('', 'Memory_check', 'toolbar=yes,scrollbars=yes,resizable=yes,top=500,left=500,width=800,height=800'); memorywindow.document.write(\"" + html + "\");"
        else:
            context["element_html"] = "$('#"+action.get("target", "pw_memory_window")+"').html(\"" + html + "\")"
    else:
        context["element_html"] += "var memorywindow = window.open('', 'Memory_check', 'toolbar=yes,scrollbars=yes,resizable=yes,top=500,left=500,width=800,height=800'); memorywindow.document.write(\"" + html + "\");"
