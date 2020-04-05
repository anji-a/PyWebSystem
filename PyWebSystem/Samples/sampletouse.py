from PyWebSystem.Samples.sampletouse1 import fun4
import PyWebSystem.Samples.pyconsample as conf


def fun1():
    conf.init()
    # global context
    s = {"a":{"a":"a"}, "b":{"b":"b"}}
    conf.session = s
    c = s["a"]
    conf.context = c
    context = conf.context
    session = conf.session
    context["c"] = {"c":"c"}
    print("F1", id(context))
    fun4(context)
    print("F1", id(context))
    print("F1", id(conf.context))

def fun2(con):
    filecode = """def fun3(con):
            global s
            global context
            context = s["b"]
            print("F3", con, context)
        """
    tagname = "fun3"
    code_obj = compile(filecode, tagname, 'exec')
    exec(code_obj, globals())
    globals()[tagname](con)
    print("F2", con, context)

if __name__ == '__main__':
    print("Popula Script start")
    fun1()
    #get_PyElement()
    print("Popula Script end")