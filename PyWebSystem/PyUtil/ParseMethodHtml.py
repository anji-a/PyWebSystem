from bs4 import BeautifulSoup
import json, sys
from PyWebSystem.PyUtil.FindHTMLChildNodes import find_child_codes

def process_parse():
    code = {"details": {"name": "Sample1"}, "methods": []}
    methods = []
    with open("C:/Users/AF86407/Documents/GitHub/PyWebSystem/PyWebSystem/PyHtml/Sample.html") as fp:
        html = BeautifulSoup(fp, "html.parser")
    #print(find_child_codes(html.contents[0], attrs={"data-find": "row"}))
    for key, element in enumerate(find_child_codes(html.contents[0], attrs={"data-find": "row"})):
        #print(element)
        method = json.loads(element['data-controlset'])
        method["method"] = {}
        if isinstance(element.find(attrs={"data-find": "method"}), dict):
            method["method"]["name"] = element.find(attrs={"data-find": "method"}).get('value', "")

        #print(element.find(attrs={"data-find": "row"}))
        submethod = []

        for key, element in enumerate(find_child_codes(element, attrs={"class": "col-12 pl-5"})):
            for subkey, subelement in enumerate(find_child_codes(element, attrs={"data-find": "row"})):
                submethod.append(sub_methods(subelement))

        method["methods"] = submethod
        #submethod = sub_methods(element.find_all(class_="row p-1", recursive=True))
        print("------------------------------------------------------------------------------------------------------------")
        methods.append(method)
    code["methods"] = methods
    print(code)


def sub_methods(element):
    #print(element)
    submethod = []
    method = json.loads(element['data-controlset'])
    method["method"] = {}
    if isinstance(element.find(attrs={"data-find": "method"}), dict):
        method["method"]["name"] = element.find(attrs={"data-find": "method"}).get('value', "")

    #print(element.find_all(class_="row p-1"))
    #submethod.append(method)
    #submethod = []
    for key, element in enumerate(find_child_codes(element, attrs={"class": "col-12 pl-5"})):
        for subkey, subelement in enumerate(find_child_codes(element, attrs={"data-find": "row"})):
            submethod.append(sub_methods(subelement))
    method["methods"] = submethod

    #submethod = sub_methods(element.find_all(class_="row p-1", recursive=True))
    #print("---------------------")
    return method



if __name__ == '__main__':
    print("Popula Script start")
    process_parse()
    # get_PyElement()
    print("Popula Script end")