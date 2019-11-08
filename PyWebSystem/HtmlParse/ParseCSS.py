from django.conf import settings
from PyWebSystem.Samples.LayoutFormatSamples import flex_inline
import json


def parseCSS():
    print(settings.STATIC_DIR)
    filename = settings.STATIC_DIR+"\css\py_dynamic.css"
    f = open(filename, "w+")

    css = ""
    cs = flex_inline()
    css += cs + "\n"
    """for key, value in a.items():
        for k, v in value.items():
            css += "."+key+"\n"
            cs = json.dumps(v).replace("\"", "").replace(",", ";")
            css += cs
            css += "\n"
    """
    f.write(css)
    f.close()
