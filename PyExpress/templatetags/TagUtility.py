from django import template
from PyWebSystem.PyUtil.treeview import tree_view
register = template.Library()


@register.simple_tag(takes_context=True)
def tag_utility(context,  *args, **kwargs):
    #print(context)
    #print(kwargs["con"], "\n................................")
    context = kwargs["con"]
    html = tree_view(context)
    return html



