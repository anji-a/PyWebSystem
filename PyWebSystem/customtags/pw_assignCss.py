from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.PyUtil.ExecuteExpression import ExecuteExpression
from PyWebSystem.customtags.pw_defineConfiguration import defineConfigurationwithkey
from PyWebSystem.Samples.LayoutFormatSamples import flex_inline
import json


def assignCss(context, *args, **kwargs):
    logmessage("assignCss", "warning", message=args[2])
    # layconf = defineConfigurationwithkey(context.get("ElementPrimary", {}), args[2])
    # layconf = flex_inline(True)
    # logmessage("assignCss", "warning", context.get("Config"))
    layconf = {}
    layconf["layvisibility"] = True
    controlset = context.get("ElementPrimary", {}).get(args[2], {})
    generalset = controlset.get("generalset", {})
    presentationset = controlset.get("presentationset", {})
    logmessage("assignCss", "warning", context.get("ElementPrimary", {}))
    controlsetstr = json.dumps(controlset)
    layconf["controlsetstr"] = controlsetstr
    layconf.update(defineGeneralSet(context, generalset, layconf))
    layconf.update(definePrasantationSet(context, presentationset, layconf))
    logmessage("assignCss", "warning", layconf)
    return layconf


def defineGeneralSet(context, generalset, layconf):
    if generalset.get("Condition", "") != "":
        layconf["layvisibility"] = ExecuteExpression(context, path=context.get("elpath", ""), condition=generalset.get("Condition", ""))
    if generalset.get("layoutformat", "") == "double":
        layconf["layclass"] = layconf.get("layclass", "") + "w3-half"
    elif generalset.get("layoutformat", "") == "triple":
        layconf["layclass"] = layconf.get("layclass", "") + "w3-third"
    if generalset.get("TitleDisplay", "") == "true":
        layconf["Titile"] = generalset.get("TitleValue", "")
        layconf["TitileType"] = generalset.get("TitileType", "")
        if layconf["TitileType"] == "Bar":
            layconf["layCss"] = layconf.get("layCss", "") + " w3-border "
    layconf["DisplayType"] = generalset.get("DisplayType", "")
    layconf["Titile"] = generalset.get('TitleValue', '')
    layconf["Active"] = generalset.get('Active', '')
    layconf["iconcss"] = generalset.get('iconcss', '')
    layconf["generalset"] = generalset
    return layconf


def definePrasantationSet(context, presentationset, layconf):
    if presentationset.get("css", "") != "":
        layconf["layCss"] = layconf.get("layCss", "") +"w3-container "+ presentationset.get("css", "")
    return layconf
