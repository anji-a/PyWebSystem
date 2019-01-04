import sys
from functools import reduce


def dick_update(key, originaldata, updatedata):
    try:
        if key in originaldata:
            originaldata[key].update(updatedata)

        else:
            originaldata[key] = updatedata
        return originaldata
    except:
        print(sys.exc_info())
        return originaldata


def process_request_dick(request={}, session={}):
    #print(session, "\n....................")
    parserequest = session
    #print(request, "\n....................")
    for key, value in request.items():
        if key.__contains__("$"):
            #standard$element
            #parserequest[standard][element]
            tempelement = parserequest

            for element in key.split('$'):

                if element is not "":
                    if element[1:] in tempelement.keys():
                        tempelement = tempelement.get(element[1:], value)
                        #print(tempelement, "\n....................")
                    elif element[0].__eq__("l") and (element.split('&')[0][1:] in tempelement.keys()):
                        tempelement = tempelement[element.split('&')[0][1:]][int(element.split('&')[1])]
                    else:
                        if element[0].__eq__("d"):
                            tempelement[element[1:]] = {}
                            tempelement = tempelement[element[1:]]
                        elif element[0].__eq__("e"):
                            tempelement[element[1:]] = value
                        elif element[0].__eq__("l"):
                            try:
                                keys = element.split('&')
                                tempelement[keys[0][1:]] = []
                                tempelement1 = tempelement[keys[0][1:]]
                                tempelement1[int(keys[1])] = {}
                                tempelement = tempelement1[keys[1]]
                            except IndexError:
                                if "pwexceptions" in parserequest.keys():
                                    parserequest["pwexceptions"].append(key+" Has index issue")
                                else:
                                    parserequest["pwexceptions"] = []
                                    parserequest["pwexceptions"].append(key + " Has index issue")
        else:
            parserequest["EventData"] = parserequest.get("EventData", {})
            parserequest["EventData"][key] = value

    #print(parserequest, "\n....................")


def get_furthest(s, path):
    '''
    Gets the furthest value along a given key path in a subscriptable structure.

    subscriptable, list -> any
    :param s: the subscriptable structure to examine
    :param path: the lookup path to follow
    :return: a tuple of the value at the furthest valid key, and whether the full path is valid
    '''

    def step_key(acc, key):
        s = acc[0]
        if isinstance(s, str):
            return (s, False)
        try:
            return (s[key], acc[1])
        except LookupError:
            return (s, False)

    return reduce(step_key, path, (s, True))


def get_val(s, path):
    val, successful = get_furthest(s, path)
    if successful:
        return val
    else:
        return None


def set_val(s, path, value):
    get_val(s, path[:-1])[path[-1]] = value


def gattr(d, *attrs):
    """
    This method receives a dict and list of attributes to return the innermost value of the give dict
    """
    try:
        for at in attrs:
            d = d[at]
        return d
    except:
        return None


"""def dict_path(path, my_dict):
    for k, v in my_dict.items():
        if isinstance(v, list):
            for i, item in enumerate(v):
                dict_path(path + "." + k + "." + str(i), item)
        elif isinstance(v, dict):
            dict_path(path+"."+k, v)
        else:
            print(path+"."+k, "=>", v)"""


def dict_path(my_dict, path=None):
    if path is None:
        path = []
    for k, v in my_dict.items():
        newpath = path + [k]
        if isinstance(v, list):
            temppath = newpath
            for i, v in enumerate(v):
                newpath = temppath + [i]
                for u in dict_path(v, newpath):
                    yield u
        elif isinstance(v, dict):
            for u in dict_path(v, newpath):
                yield u
        else:
            yield newpath, v, k


def dict_loop(dict={}, path=""):
    for key, value in dict.items():
        yield key, value, path+"$d"+key


def list_loop(listobj=[], path=""):
    for key, value in enumerate(listobj):
        yield key, value, path+"$l"+str(key)


def key_list(key=""):
    key = key.split('$')
    #print(key)
    keylist = []
    for k in key:
        if k != "":
            keylist.append(k[1:])
    return keylist

if __name__ == '__main__':
    print("Popula Script start")#pr[standard][results][1][name]
    code_dick = {"$dstandard$pname": "sample", "$dstandard$pdir": "code", "name": "hello","$dstandard$lresults&1$pname": "ohh"}
    session = {"standard": {"results": [{"a": "a"}, {"b": "b"}]}, "name": "hi"}
    #print(sattr(session, ["standard", "results", "1", "b"], {"a": "b"}))
    #print(get_val(session, ["standard", "results", 1, "c"]))
    #for k, v, p in dict_loop(session):
        #print(k, v, p)
    # get_PyElement()
    print(key_list("$dstandard$pname"))
    print("Popula Script end")