

x = 10

code5 = {"details": {"name": "Sample"}, "methods": [
    {
        "begin-condition": [
            {},
        ],
        "loop": {

        },
        "method": {
            "name": "Property-Set",
            "value": [{"to": "x", "from": "10"}, ]
        },
        "end-condition": [
            {},
        ]
    }
]}

class Sample:
    def __init__(self, global_dict={}, local_dict={}, dick={}, params={}, *args, **kwargs):
        self.global_dict = global_dict
        self.local_dict = local_dict
        self.dick = dick
        self.params = params
        self.args = args
        self.kwargs = kwargs

    def process(self):
        if x == 10:
            self.sam()
            Sample1().process()
            #print(c1)

    def sam(self):
        #print(self.params)
        c1 = {}
        b = x == 20
        c1 = code5.get("details").copy()
        print(c1)
        c1["sam"] = "HI"
        print(code5)
        print(c1)
        print(b)
