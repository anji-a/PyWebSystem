from django.core.cache import cache
import sys
import json
from PyWebSystem.PyUtil.DickUpdate import process_request_dick


def get_session(sessionid=None):
    if sessionid is None:
        return False
    else:
        try:

            if sessionid in cache:
                session = cache.get(sessionid)
                return session
            else:
                cache.set(sessionid, {"sessionid": sessionid})
                session = cache.get(sessionid)
                return session
        except:
            print("Exception occur", sys.exc_info())


def update_session(session=None):
    try:
        if session is not None:
            if session.get("sessionid", None) is not None:
                #print(session, "\n.......")
                cache.set(session.get("sessionid"), session)
                #print(cache.get(session.get("sessionid")), "\n....")
    except:
        print("update session exception", sys.exc_info())


def update_request(request=None, session={}, *args, **kwargs):
    kwargs.get("params", {})["sessionid"] = request.session.session_key
    my_dic = request.POST.dict()
    #print(my_dic)
    controlset = json.loads(my_dic.get("data-controlset", '{}'))
    my_dic["data-controlset"] = controlset
    #print(my_dic)
    #session = get_session(request.session.session_key)
    root_obj = session.get(my_dic.get("data-controlset", {}).get("root_data", session.get("Requester", "").get("sessionid", "")), {})
    process_request_dick(my_dic, root_obj)
    context = root_obj
    #print(session)
    return context


def get_session_by_context(context={}):
    sesssionid = context.get("Requester", {}).get("sessionid", "")
    if sesssionid is "":
        return None
    else:
        if sesssionid in cache:
            return cache.get(sesssionid)
        return None
