

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



if __name__ == '__main__':
    print("Popula Script start")
    executecode("C:/Users/AF86407/Documents/GitHub/PyWebSystem/PyWebSystem/PyUtil/Sample.py",
                "C:/Users/AF86407/Documents/GitHub/PyWebSystem/PyWebSystem/PyUtil/Sample1.py")
    # get_PyElement()
    print("Popula Script end")