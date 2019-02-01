from django.template.loader import render_to_string


def render_html(context={}):
    html = render_to_string('PyWeb/pw_screen_render.html', context={"context": context})

    html = "".join([line.strip("\n\t") for line in html])
    #print(html)
    html = html.replace('"', '\\"')
    html = html.replace("/*", "\\/*")
    html = html.replace("*/", "*\\/")
    return html
