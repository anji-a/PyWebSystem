code = {"methods": [{"b": 1}, {"methods": [{"b": 2}, {"methods": [{"b": 3}]}]}]}

code_dick = {"details": {"name": "Sample1"}, "methods": [
    {
        "begin-condition": [
            {"condition": "x == 10", "if_true": "proceed", "if_false": "skip_method"},
            {"condition": "y == 10", "if_true": "skip_condition", "if_false": "goto"},
        ],
        "loop": {
            "enable": "true",
            "type": "dick",
        },
        "method": {
            "name": "Property-Set",
            "value": [{"to": "x", "from": "10"}, ],
            "methods": [
                {
                    "begin-condition": [],
                    "loop": {
                        "enable": "true",
                        "type": "dick",
                    },
                    "method": {
                        "name": "Property-Set",
                        "value": [{"to": "y", "from": "10"}, ],
                        "methods": [
                            {
                                "begin-condition": [],
                                "loop": {
                                    "enable": "true",
                                    "type": "dick",
                                },
                                "method": {
                                    "name": "Property-Set",
                                    "value": [{"to": "z", "from": "10"}, ]
                                },
                                "end-condition": [
                                    {},
                                ]
                            }
                        ]
                    },
                    "end-condition": [
                        {},
                    ]
                }
            ]
        },
        "end-condition": [
            {},
        ]
    }
]}


code_ex1 = {"details": "Sample",
            "methods": [
                {
                    "method": {"name": "F1"}
                },
                {
                    "method": {"name": "F2",
                               "methods": [
                                   {
                                       "method": {"name": "F2F1"}
                                   },
                                   {
                                       "method": {"name": "F2F2",
                                                  "methods": [
                                                      {
                                                          "method": {"name": "F2F2F1"}
                                                      }
                                                  ]}
                                   },
                                   {
                                       "method": {"name": "F2F3"}
                                   }
                               ]
                               },
                    "method": {"name": "F3"}
                },
            ]}

def defff(code1):
    for index, method in code1.items():
        print(method[0], len(method))
        if len(method) > 1:
            defff(method[1])
        print(method[0])


def defff2(code1):
    #print(code1)
    #defff(code)
    for idx, method in enumerate(code1.get("methods", {})):
        #print(method, len(method))
        defff2(method.get("method"))
        print(method.get("method").get("value"))
       # if len(method) > 1:
        #    defff2(method)
        #print(method[0])




if __name__ == '__main__':
    print("Popula Script start")
    defff2(code_dick)
    # get_PyElement()
    print("Popula Script end")