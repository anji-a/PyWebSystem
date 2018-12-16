from DefineConditions import define_conditions
from DefineMethods import define_method
#from DefineFunctionSequence import function_sequence

def define_functions(_tabs={}, function_index=0, func={}):
    def_method = []
    function_tab = _tabs.get("class_tab") + "\t"
    _tabs["function_tab"] = function_tab
    def_fun = _tabs.get("class_tab") + "def "+_tabs.get("Parent_fun", "")+"fun"+str(function_index)+"(self):"+function_tab
    for condition_index, condition in enumerate(func.get("begin-condition", {})):
        def_fun += define_conditions(_tabs, condition_index, condition, func.get("method"))
    #def_fun += function_sequence(_tabs, func.get("method").get("methods", {}))
    _tabs["Parent_fun"] = "fun" + str(function_index)
    for methodindex, method in enumerate(func.get("method").get("methods", {})):
        _tabs["Parent_fun"] = "fun" + str(function_index)
        def_method = define_functions(_tabs, methodindex, method)
        _tabs["Parent_fun"] = ""
    def_method.append(def_fun)

    return def_method


def define_functions_v1(_tabs={}, method={}, parent="", function_index=""):
    def_method = []
    function_tab = _tabs.get("class_tab") + "\t"
    _tabs["function_tab"] = function_tab
    def_fun = _tabs.get("class_tab") + "def "+parent+"fun"+str(function_index)+"(self):"+function_tab
    if method.get("begin-condition", {}) != {}:
        for condition_index, condition in enumerate(method.get("begin-condition", {})):
            def_fun += define_conditions(_tabs, condition_index, condition, method.get("method"))
    else:
        def_fun += define_method(_tabs, method.get("method", {}))

    return def_fun