from DefineMethods import define_method

def define_conditions(_tabs={}, condition_index=0, condition={}, method={}):
    condition_tab = _tabs.get("function_tab") + "\t"
    function_tab = _tabs.get("function_tab")
    _tabs["condition_tab"] = condition_tab
    defcondition = "c" + str(condition_index) + " = " + condition.get("condition") + function_tab
    def_condition = ""
    def_condition += defcondition
    if condition.get("if_true") == "proceed":
        deftruecondition = "if c" + str(condition_index) + " == \"True\":"+condition_tab
        def_condition += deftruecondition + "pass"+function_tab
    if condition.get("if_true") == "skip_method":
        deftruecondition = "if c" + str(condition_index) + " == \"True\":"+condition_tab
        def_condition += deftruecondition + "pass"+function_tab
    if condition.get("if_true") == "skip_condition":
        deftruecondition = "if c" + str(condition_index) + " == \"True\":"+condition_tab
        def_condition += deftruecondition + define_method(_tabs, method.get("method", {}))


    if condition.get("if_true") == "goto":
        deftruecondition = "if c" + str(condition_index) + " == \"True\":"+condition_tab
        def_condition += deftruecondition + "pass"+function_tab
    if condition.get("if_false") == "proceed":
        deffalsecondition = "if c" + str(condition_index) + " == \"False\":"+condition_tab
        def_condition += deffalsecondition + "pass"+function_tab
    if condition.get("if_false") == "skip_method":
        deffalsecondition = "if c" + str(condition_index) + " == \"False\":"+condition_tab
        def_condition += deffalsecondition + "pass"+function_tab
    if condition.get("if_false") == "skip_condition":
        deffalsecondition = "if c" + str(condition_index) + " == \"False\":"+condition_tab
        def_condition += deffalsecondition + define_method(_tabs, method.get("method", {}))
    if condition.get("if_false") == "goto":
        deffalsecondition = "if c" + str(condition_index) + " == \"False\":"+condition_tab
        def_condition += deffalsecondition + "pass"+function_tab

    return def_condition
