import json


def convertStrToDict(context, *args, **kwargs):
    #print("....", args[2][0], args[3][0])
    strb = args[2]
    strb =strb[:strb.__len__()-1]
    strb = strb[1:]
    return json.loads(strb)
