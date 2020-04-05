import PyWebSystem.Samples.pyconsample as conf

def fun4(con):
    global conf
    print("F4", con)
    con = conf.session["b"]
    conf.context = con
    print("F4", id(conf.context))


