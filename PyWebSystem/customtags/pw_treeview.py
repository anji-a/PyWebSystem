from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.PyUtil.DickUpdate import pw_loop
from PyWebSystem.PyUtil.pw_extra_methods import id_generator


def treeview(context, *args, **kwargs):
    # logmessage("treeview", "warning", context)
    parentid = id_generator(6)
    html = "<ul id=" + parentid + ">"
    for index, key, path, value in pw_loop(context.__dict__["dicts"][1]):
        if type(value) in [dict, list] and key != "selected_dick":
            html += '<li data-key=' + path[1:] + ' onclick="processeventaction(event)" data-controlset=\'{"actionset":[{"event":"click","eventdata":[{"action":"refresh_memory", "purpose":"pw_memory", "target":"divId","select_dict":"' + path[1:] + '"}]}]}\' >' + key
            html += loopsubdict(value, path[1:])
            html += "</li>"
    html += "</ul>"
    html += "<script>$('#" + parentid + "').treed(); function abc(){$('#divId').load(location.href + ' #divId>*', '');console.log('HI')}</script>"
    return html


def loopsubdict(value, parentpath):
    html = "<ul>"
    # for key, value in dick.items():
    for index, key, path, value in pw_loop(value):
        if type(value) is dict and key != "selected_dick":
            html += '<li data-key=' + parentpath+path + ' onclick=processeventaction(event) data-controlset=\'{"actionset":[{"event":"click","eventdata":[{"action":"refresh_memory", "purpose":"pw_memory", "target":"divId","select_dict":"' + parentpath+path + '"}]}]}\'>' + key
            html += loopsubdict(value, parentpath+path)
            html += "</li>"
    html += "</ul>"
    return html
