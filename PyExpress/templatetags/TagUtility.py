from django import template
from PyWebSystem.PyUtil.treeview import treeview
from PyWebSystem.PyUtil.ExecuteCode import exe_code_from_local
register = template.Library()


@register.simple_tag(takes_context=True)
def tag_utility(context,  *args, **kwargs):
    #print(kwargs)
    #print(kwargs["con"], "\n................................")
    #context = kwargs["con"]
    #html = treeview(context)
    html = exe_code_from_local(context, *args, **kwargs)
    return html
