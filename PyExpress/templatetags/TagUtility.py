from django import template
from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.customtags.pw_addpath import addpath
from PyWebSystem.PyUtil.ExecuteCode import exe_code_from_local, exe_tag_from_local
register = template.Library()


@register.simple_tag(takes_context=True)
def tag_utility(context,  *args, **kwargs):
    """
        used to call some method tag
    :param context:
    :param args:
    :param kwargs:
    :return:
    """
    #print(context)
    kwargs["scope"] = context
    #print(kwargs["scope"])
    html = exe_code_from_local(context, *args, **kwargs)
    return html


@register.tag
def includeBlockTag(parser, token):
    """
    used to call block tag and will return HTML
    :param parser:
    :param token:
    :return:
    """
    logmessage(__name__+",includeBlockTag", "warning", token.split_contents())
    #tag, tag_name, config = token.split_contents()
    #tag = "includeTag "+tag_name
    nodelist = parser.parse(('endincludeBlockTag',))
    parser.delete_first_token()
    return UpperNode(nodelist, {"aa": "bb"})

@register.tag
def includeTag(parser, token):
    """
    used to call as Tag and will render HTML
    :param parser:
    :param token:
    :return:
    """
    #print(__name__)
    #logmessage(__name__+",includeTag", "warning", token.split_contents())
    #tag, tag_name, config = token.split_contents()
    #tag = "includeTag "+tag_name
    #nodelist = parser.parse(('endincludeTag',))
    #parser.delete_first_token()
    return RenderTag(token.split_contents())


class RenderTag(template.Node):
    def __init__(self, kwargs):
        self.kwargs = kwargs
        self.returnvalue = True
        if kwargs[-2] == "as":
            self.varname = kwargs[-1]
            self.returnvalue = False

    def render(self, context):
        #print("2...", self.returnvalue)
        #exe_tag_from_local(context, self.kwargs)
        #output = self.nodelist.render(context)
        if self.returnvalue:
            return exe_tag_from_local(context, self.kwargs)
        else:
            returnresult = exe_tag_from_local(context, self.kwargs)
            context[self.varname] = returnresult
            #print(context[self.varname], self.varname)
            return ''


class UpperNode(template.Node):
    def __init__(self, nodelist, kwargs):
        self.nodelist = nodelist
        self.kwargs = kwargs
        print(kwargs)

    def render(self, context):
        print(self.nodelist, self.kwargs)
        output = self.nodelist.render(context)
        return output.upper()


@register.filter
def index(indexable, i):
    return indexable[i]


@register.filter
def add_flower(value, path):
    if value == "" or value is None:
        return ""
    else:
        return '{{ '+path+'%s }}' % value


@register.filter
def add_path(value, path):
    return addpath(value, path)
