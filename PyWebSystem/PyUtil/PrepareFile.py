from ExecuteCode import executecode
from UnZipGZfile import unzip_gz_file
from GeneratePython import GeneratePython

code_dick = {"details": {"name": "Sample1"},
             "methods": [
                 {
                     "method": {"name": "F1"}
                 },
                 {
                     "loop": {
                     "enable": "true",
                     "type": "dick",
                    },
                     "method": {"name": "F2",
                                "methods": [
                                    {
                                        "method": {"name": "F2F1"}
                                    },
                                    {
                                        "loop": {
                                            "enable": "true",
                                            "type": "dick",
                                        },
                                        "method": {"name": "F2F2",
                                                   "loop": {
                                                       "enable": "true",
                                                       "type": "dick",
                                                   },
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
                 },
                 {"method": {"name": "F3"}}
             ]}


def writefile():
    code = 'def sam():\n\tprint("hello")\n\tprint("world")\n'
    file = open("C:/Users/AF86407/Documents/GitHub/PyWebSystem/PyWebSystem/PyUtil/Sample1.py", "w+")
    # file.write(code)
    # file.close()
    # print(code_dick)
    generatepython = GeneratePython(code_dick)
    code = generatepython.start_process()
    file.write(code)
    file.close()
    executecode(filename="Sample1.py")


if __name__ == '__main__':
    print("Popula Script start")
    writefile()
    # get_PyElement()
    print("Popula Script end")
