import random
import string
from PyWebSystem.PyUtil.DickUpdate import dict_loop, list_loop
from PyWebSystem.PyUtil.pw_logger import logmessage


def treeview(context={}, *args, **kwargs):
    logmessage("treeview", "warning", context.__dict__)
    con = context.__dict__
    id = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
    html = "<ul id="+id+">"
    #onclick="processevent(event)" data-controlset='{"element":"pw_memory","data_element":"static","actiontype":"window"}'
    #for key, value in context.items():
    for key, value, path in dict_loop(con["dicts"][1]):
        if type(value) is dict and key != "selected_dick":
            html += '<li data-key='+path+' onclick="processeventaction(event)" data-controlset=\'{"actionset":[{"event":"click","eventdata":[{"action":"refresh_memory", "purpose":"pw_memory", "target":"divId","select_dict":"'+path+'"}]}]}\' >'+key
            html += loopdict(value, path)
            html += "</li>"
    html += "</ul>"
    html += "<script>$('#"+id+"').treed(); function abc(){$('#divId').load(location.href + ' #divId>*', '');console.log('HI')}</script>"
    return html


def loopdict(dick={}, path=""):
    html = "<ul>"
    #for key, value in dick.items():
    for key, value, path in dict_loop(dick, path):
        if type(value) is dict and key != "selected_dick":
            html += '<li data-key='+path+' onclick=processeventaction(event) data-controlset=\'{"actionset":[{"event":"click","eventdata":[{"action":"refresh_memory", "purpose":"pw_memory", "target":"divId","select_dict":"'+path+'"}]}]}\'>'+key
            html += loopdict(value, path)
            html += "</li>"
    html += "</ul>"
    return html
