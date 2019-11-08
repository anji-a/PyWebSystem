from django.template.loader import render_to_string
from django.template import Context, Template


def render_html(context={}):
    #print("........", context.get("element", ""))
    if context.get("data_element", '') == "static":
        html = render_to_string('PyWeb/pw_screen_render.html', context={"context": context})
    else:

        t = Template(context.get("element", ""))
        c = Context(context)
        #print(c)
        html = t.render(c)
    html = "".join([line.strip("\n\t") for line in html])
    #print(html)
    html = html.replace('"', '\\"')
    html = html.replace("/*", "\\/*")
    html = html.replace("*/", "*\\/")
    #openmodelwindow(event, displayhtml)
    html = "openmodelwindow(event,\""+html+"\")"
    return html



