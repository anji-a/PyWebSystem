from PyWebSystem.PyUtil.pw_logger import logmessage

def exe_code_from_local(context, *args, **kwargs):
    context = kwargs.get("scope", {})
    tagname = kwargs.get("pw_tag", "")
    #print(kwargs)
    if tagname is not "":
        filename = "C:/Users/anjaneyulu_a/Documents/Python/Apache/htdocs/WebSystem/PyWebSystem/PyUtil/"+tagname+".py"
        fileopen = open(filename, "r")
        filecode = fileopen.read()
        fileopen.close()
        code_obj = compile(filecode, tagname, 'exec')
        exec(code_obj, locals())
        #print(kwargs)
        return locals()[tagname](context, *args, **kwargs)


def exe_tag_from_local(context, args):
    #context = kwargs.get("scope", {})
    tagname = args[1]
    #print(kwargs)
    kwargs = {}
    if tagname is not "":
        filename = "C:/Users/anjaneyulu_a/Documents/Python/Apache/htdocs/WebSystem/PyWebSystem/customtags/pw_"+tagname+".py"
        fileopen = open(filename, "r")
        filecode = fileopen.read()
        fileopen.close()
        code_obj = compile(filecode, tagname, 'exec')
        exec(code_obj, locals())
        #print(kwargs)
        return locals()[tagname](context, *args, **kwargs)


def executecode(filename1, filename2):
    file1 = open(filename1, "r")
    code1 = file1.read()
    file1.close()
    file2 = open(filename2, "r")
    code2 = file2.read()
    file2.close()
    finalCode = code2+code1
    code_obj = compile(finalCode, "Sam", 'exec')
    exec(code_obj, locals())
    dick1 = {"a": 10}
    locals()["Sample"](dick=dick1).process()
    #locals()["sam"]()


def executeaction(context={}, action={}, *args, **kwargs):
    logmessage(__name__, "warning")
    #print("hello", action)
    tagname = action.get("actionname", "")
    filename = "C:/Users/anjaneyulu_a/Documents/Python/Apache/htdocs/WebSystem/PyWebSystem/PyUtil/" + tagname + ".py"
    fileopen = open(filename, "r")
    filecode = fileopen.read()
    fileopen.close()
    code_obj = compile(filecode, tagname, 'exec')
    exec(code_obj, locals())
    return locals()[tagname](context, action, *args, **kwargs)
    pass


if __name__ == '__main__':
    print("Popula Script start")
    executecode("C:/Users/AF86407/Documents/GitHub/PyWebSystem/PyWebSystem/PyUtil/Sample.py",
                "C:/Users/AF86407/Documents/GitHub/PyWebSystem/PyWebSystem/PyUtil/Sample1.py")
    # get_PyElement()
    print("Popula Script end")