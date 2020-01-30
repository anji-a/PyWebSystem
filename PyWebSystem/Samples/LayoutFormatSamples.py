

def flex_inline(returncsstypes=False):
    csstypes = {
        "layout": "flex-content-inline",
        "element": "content-item",
        "Item_Spacing": "field-caption",
    }
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
    if returncsstypes:
          return csstypes
    else:
          return css


def StandardTab(returncsstypes=False):
    csstypes = {
        "tagGroup": "ST_Tabgroup",
        "tabHeader": "ST_tabsheader",
        "tabContent": "ST_tab-content"
    }
    css = ".fade {opacity: 0;.transition(opacity .15s linear);&.in {opacity: 1;}}\n" \
          ".ST_Tabgroup {padding-left: 0;margin-bottom: 0;  list-style: none;  &:extend(.clearfix all);  " \
          "\n> li {position: relative;display: block;" \
          "\n> a {position: relative;display: block;padding: @nav-link-padding;" \
          "\n&:hover,&:focus{text-decoration: none;background-color: @nav-link-hover-bg;}}" \
          "\n&.disabled > a {color: @nav-disabled-link-color;" \
          "\n&:hover,&:focus {color: @nav-disabled-link-hover-color;text-decoration: none;cursor: @cursor-disabled;background-color: transparent;}}}}" \
          "\n.ST_tabsheader {border-bottom: 1px solid @nav-tabs-border-color;" \
          "\n> li {float: left;margin-bottom: -1px;" \
          "\n> a {margin-right: 2px;line-height: @line-height-base;border: 1px solid transparent;border-radius: @border-radius-base @border-radius-base 0 0;" \
          "\n&:hover {border-color: @nav-tabs-link-hover-border-color @nav-tabs-link-hover-border-color @nav-tabs-border-color;}}" \
          "\n&.active > a {" \
          "\n&,&:hover,&:focus {color: @nav-tabs-active-link-hover-color;cursor: default;background-color: @nav-tabs-active-link-hover-bg;border: 1px solid @nav-tabs-active-link-hover-border-color;border-bottom-color: transparent;}}}" \
          "\n&.nav-justified {.nav-justified();.nav-tabs-justified();}}" \
          "\n.ST_tab-content {" \
          "\n> .tab-pane {display: none;}" \
          "\n> .active {display: block;}}"
    if returncsstypes:
          return csstypes
    else:
          return css
