from DefineFunctions import define_functions_v1


def function_sequence(_tabs={}, methods={}):
    current_tab = _tabs.get("current_tab")
    def_sequence = ""
    for method_idx, method in enumerate(methods):
        loop_tab = current_tab+"\t"
        if method.get("loop", {}).get("enable") == "true":
            if method.get("loop").get("type") == "dick":
                def_sequence += "for loopindex, element in self.dick.items():" + loop_tab +\
                                "''' Step " + str(method_idx) + "define'''" + loop_tab + \
                                "self."+_tabs.get("Parent_fun", "")+"fun" + str(method_idx) + "()"+current_tab
        else:
            def_sequence += "''' Step " + str(method_idx) + "define'''" + current_tab + "self."+_tabs.get("Parent_fun", "")+"fun" + str(method_idx) + \
                            "()" + current_tab
    return def_sequence


def function_sequence_v1(_tabs={}, method={}, parent="", index=""):
    def_fun = ""
    def_fun += define_functions_v1(_tabs, method, parent, index)
    def_name = parent+"fun"+str(index)
    if method.get("method", {}).get("methods", {}) != {}:
        for methodindex, method in enumerate(method.get("method", {}).get("methods", {})):
            function_sequence_v1(_tabs, method, def_name, methodindex)
            loop_tab = _tabs.get("current_tab") + "\t"
            if method.get("loop", {}).get("enable") == "true":
                if method.get("loop").get("type") == "dick":
                    def_fun += "for loopindex, element in self.kwargs.items():" + loop_tab + \
                                    "''' Step " + str(methodindex) + "define'''" + loop_tab + \
                                    "self." + def_name + "fun" + str(methodindex) + "()" + _tabs.get("current_tab")
            else:
                def_fun += _tabs.get("current_tab") + "''' Step " + str(methodindex) + "define'''" + _tabs.get("current_tab") + "self." + def_name + "fun" + str(methodindex) + \
                                "()" + _tabs.get("current_tab")
    _tabs.get("methods").append(def_fun)
