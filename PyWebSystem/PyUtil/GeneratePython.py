from DefineFunctions import define_functions
from DefineFunctionSequence import function_sequence, function_sequence_v1
class GeneratePython:

    def __init__(self, code):
        self.tabcount = 0
        self.code = code
        self.generatedcode = []
        self.tabs = ""

    def start_process(self):
        print(self.tabcount)
        print(self.code)

        name = self.code.get("details").get("name")
        #classcode = "from django.core.cache import cache\n\nclass "+name+":\n\t"
        classcode = "import traceback\n\nclass "+name+":\n\t"
        definit = "def __init__(self, sessionid={}, params={}, *args, **kwargs):\n\t\t" \
                              "self.sessionid = sessionid\n\t\t" \
                              "self.params = params\n\t\t" \
                              "self.args = args\n\t\t" \
                              "self.kwargs = kwargs\n\n\t"
        self.generatedcode.append(classcode+definit)
        _tabs = {"class_tab": "\n\t"}
        # Define Process Function
        _tabs["process_tab"] = _tabs.get("class_tab") + "\t"
        _tabs["current_tab"] = _tabs.get("process_tab")
        _tabs["methods"] = []
        defprocess = "def process(self):" + _tabs.get("process_tab")
        for methodindex, method in enumerate(self.code.get("methods")):
            function_sequence_v1(_tabs, method, "", methodindex)
            loop_tab = _tabs.get("current_tab") + "\t"
            if method.get("loop", {}).get("enable") == "true":
                if method.get("loop").get("type") == "dick":
                    defprocess += "for loopindex, element in self.kwargs.items():" + loop_tab + \
                                    "''' Step " + str(methodindex) + "define'''" + loop_tab + \
                                    "self.fun" + str(methodindex) + "()" + _tabs.get("current_tab")
            else:
                defprocess += "''' Step " + str(methodindex) + "define'''" + _tabs.get("current_tab") + "self.fun" + str(methodindex) + \
                                "()" + _tabs.get("current_tab")
        self.generatedcode.append(defprocess)
        self.generatedcode.extend(_tabs.get("methods"))
        # Define Functions
        for methodindex, method in enumerate(self.code.get("methods")):
            defmethods = define_functions(_tabs, methodindex, method)
            print(_tabs.get("Parent_fun"))
            #self.generatedcode.extend(defmethods)
        gencode = ""
        #print(self.generatedcode)
        for value in self.generatedcode:
            gencode += value

        return gencode