from PyWebSystem.PyUtil.pw_logger import logmessage
import re
import sys
from PyWebSystem.PyUtil.DickUpdate import get_dictvalue


def ExecuteExpression(context, **kwargs):
    logmessage("ExecuteExpression", "warning")
    path = kwargs.get("path", "")
    condition = kwargs.get("condition", "")
    logmessage("ExecuteExpression", "warning", condition)
    expression = preparecondition(context, path, condition)
    logmessage("ExecuteExpression", "warning", expression)
    try:
        logmessage("ExecuteExpression", "warning", eval(expression))
        result = eval(expression)
        return result
    except:
        logmessage("ExecuteExpression", "warning", sys.exc_info())
        return None


def preparecondition(context, path, condition):
    expression = ""
    conlist = re.findall('\[[^\]]*\]|\([^\)]*\)|\"[^\"]*\"|\S+', condition)
    logmessage("ExecuteExpression", "warning", conlist)
    for key, value in enumerate(conlist):
        if value[0] == "(":
            expression += "( "+definecondition(context, value, path)+" ) "
        elif value.upper() in ["AND", "OR", "&&", "||"]:
            if value.upper() == "AND" or value.upper() == "&&":
                expression += " and "
            elif value.upper() == "OR" or value.upper() == "||":
                expression += " or "
        elif value.__contains__("=="):
            if len(value) == 2:
                con = conlist[key-1]+value+conlist[key+1]
            else:
                con = value
            expression += defineexpression(context, con, path, "==")
        elif value.__contains__(">="):
            if len(value) == 2:
                con = conlist[key-1]+value+conlist[key+1]
            else:
                con = value
            expression += defineexpression(context, con, path, ">=")
        elif value.__contains__("<="):
            if len(value) == 2:
                con = conlist[key-1]+value+conlist[key+1]
            else:
                con = value
            expression += defineexpression(context, con, path, "<=")
        elif value.__contains__("!="):
            if len(value) == 2:
                con = conlist[key-1]+value+conlist[key+1]
            else:
                con = value
            expression += defineexpression(context, con, path, "!=")
        elif value.lower() == "true":
            expression += " True "
        elif value.lower() == "flase":
            expression += " False "
    return expression


def definecondition(context, condition, path):
    expression = ""
    conlist = re.findall('\[[^\]]*\]|\([^\)]*\)|\"[^\"]*\"|\S+', condition[1:condition.__len__()-1])
    for key, value in enumerate(conlist):
        if value[0] == "(":
            expression += " ( " + definecondition(context, value, path) + " ) "
        elif value.upper() in ["AND", "OR", "&&", "||"]:
            if value.upper() == "AND" or value.upper() == "&&":
                expression += " and "
            elif value.upper() == "OR" or value.upper() == "||":
                expression += " or "
        elif value.__contains__("=="):
            if len(value) == 2:
                con = conlist[key-1]+value+conlist[key+1]
            else:
                con = value
            expression += defineexpression(context, con, path, "==")
        elif value.__contains__(">="):
            if len(value) == 2:
                con = conlist[key-1]+value+conlist[key+1]
            else:
                con = value
            expression += defineexpression(context, con, path, ">=")
        elif value.__contains__("<="):
            if len(value) == 2:
                con = conlist[key-1]+value+conlist[key+1]
            else:
                con = value
            expression += defineexpression(context, con, path, "<=")
        elif value.__contains__("!="):
            if len(value) == 2:
                con = conlist[key-1]+value+conlist[key+1]
            else:
                con = value
            expression += defineexpression(context, con, path, "!=")
    return expression


def defineexpression(context, condition, path, symbal):
    expression = ""
    condititonlist = condition.split(symbal)
    for key, value in enumerate(condititonlist):
        if value.__contains__("."):
            if value[0] == ".":
                expression += "get_dictvalue(context, '"+path+value+"')"
            elif value[0] == "'" or value[0] == '"':
                expression += value
            else:
                expression += "get_dictvalue(context, '"+value+"')"
        else:
            expression += value
        if key == 0:
            expression += " "+symbal+" "
    return expression


if __name__ == '__main__':
    ExecuteExpression({}, condition=" Config.ElementSettings.elementType=='LayoutGroup' ")
