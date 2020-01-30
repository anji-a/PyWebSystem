from PyWebSystem.PyUtil.pw_logger import logmessage
from PyWebSystem.customtags.pw_defineConfiguration import defineConfigurationwithkey
from PyWebSystem.Samples.LayoutFormatSamples import flex_inline


def assignCss(context, *args, **kwargs):
    logmessage("assignCss", "warning", message=args[2])
    layconf = defineConfigurationwithkey(context.get("config"), args[2])
    layconf = flex_inline(True)
    return layconf

