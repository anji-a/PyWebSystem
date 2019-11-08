

def flex_inline():
    """css = {
        "layout": {
            "layout-inline": {
                "display": "flex",
                "flex-flow": "row wrap",
                "width": "100%",
                "min-width": "0",
                "max-width": "None"
            }
        },
        "label": {},
        "Item_Spacing": {},
    }"""
    css = ".flex-content-inline{" \
          "width:100.0%;" \
          "min-width:0;" \
          "max-width:none;" \
          "display:flex;" \
          "flex-flow:row wrap;}\n" \
          ".flex-content-inline>.content-item {display:flex;" \
          "margin: 0px 0.5em 0.5em 0px;" \
          "padding:0px;" \
          "min-height:30.0px;" \
          "width:auto;" \
          "min-width:0.0px;" \
          "flex-direction:column;" \
          "justify-content:flex-start;" \
          "align-items:flex-start;}\n" \
          ".flex-content-inline>.content-item>.field-caption {" \
          "text-align:left;" \
          "width:100%;" \
          "padding-bottom:0.0px;" \
          "flex:none;" \
          "padding-right:0px;" \
          "display:block;}"
    return css
