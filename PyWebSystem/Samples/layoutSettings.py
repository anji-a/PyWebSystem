import PyWebSystem.Samples.SectionExamples as sam
import PyWebSystem.Samples.LayoutSamples as lay


def layoutSettings(type):
    ## Settings Layout example
    LayoutSetting = {}
    deferload = {"deferload": "Defer Load Contents"}
    layoutformat = {"Default": "Default", "inline": "Inline", "double": "Double", "triple": "Triple"}
    dropdownlayoutformat = {'controlset': {}, 'controltype': 'select', 'property': '.layoutformat',
                            'sourcelist': layoutformat, "Label": "Layout Format"}
    containerformat = {"None": "None", "Default": "Default", "actionarea": "ActionArea"}
    dropdowncontainer = {'controlset': {}, 'controltype': 'select', 'property': '.containerformat',
                         'sourcelist': containerformat, "Label": "Container Format"}
    visibility = {"always": "Always", "Condition": "Condition"}
    dropdownvisibility = {'controlset': {}, 'controltype': 'select', 'property': '.visibility',
                          'sourcelist': visibility, "Label": "Visibility"}
    deferload = {'controlset': {}, 'controltype': 'radio', 'property': '.deferload', 'sourcelist': deferload}
    glayout = {"controltype": "Layout", 'controlset': {"layoutformat": "double"},
               "columns": [dropdowncontainer, dropdownlayoutformat, dropdownvisibility, deferload]}
    gt = {"controlset": {}, "PrimaryNode": ".General", "TabName": "General", "tabstatus": "active",
          "columns": [glayout, ]}

    flot = {"None": "None", "Left": "Left", "Right": "Right"}
    dropdownflot = {'controlset': {}, 'controltype': 'select', 'property': '.flot',
                    'sourcelist': flot, "Label": "Flot"}
    inlinestyle = {"controlset": {}, "controltype": "Input", "Label": "Inline Style", "property": ".style"}
    customcss = {"controlset": {}, "controltype": "Input", "Label": "Custom CSS", "property": ".css"}
    playout = {"controltype": "Layout", "columns": [dropdownflot, inlinestyle, customcss]}


    savebutton = {"controltype": "button", "Label": "Save", "onclick": "processeventaction(event)", "controlset": '{"actionset": [{"event": "click", "eventdata": [{"action": "exeaction", "actionname": "resetsettings_for_element", "Actiontype":"SaveSettings"}]}]}'}
    closebutton = {"controltype": "button", "Label": "Close", "onclick": "processeventaction(event)", "controlset": '{"actionset": [{"event": "click", "eventdata": [{"action": "Close"}]}]}'}

    footerlayout = {"controlset": {}, "controltype": "Layout", "columns": [savebutton, closebutton]}
    #Dynamic Tab repeat
    LaySample = {"controltype": "Layout", "columns": [customcss, dropdownflot, ]}
    dynamictab = {"controlset": {}, 'controltype': 'TabGroup', "TabType": "Dynamic", "TabName": "Name",
                  "TabNode": "Standard.Person", "columns": [LaySample, ]}
    #Layout repeat
    event = {"1": "Click", "2": "Hover", "3": "Double Click", "4": "Right Click"}
    actions = {"1": "Run Method", "2": "Open Model Window", "3": "Close"}
    Label = {"controlset": {}, "controltype": "Label", "property": ".Number"}
    eventDrop = {'controlset': {}, 'controltype': 'select', 'property': '.Event',
                    'sourcelist': event, "Label": "Select Event"}
    actionDrop = {'controlset': '{"actionset": [{"event": "change", "eventdata": [{"action": "refreshsection"}]}]}', 'controltype': 'select', 'property': '.Action',
                    'sourcelist': actions, "Label": "Select Action"}
    ActionLay = {"controltype": "Layout", 'controlset': {"layoutformat": "double", "Condition": ".Action=='2'"}, "columns": [inlinestyle, customcss]}
    LayHeader = {"controltype": "Layout", "columns": [Label, ]}
    ActionLayout = {"controltype": "Layout", "columns": [actionDrop, lay.OpenModelwindowLay, lay.RunMethodLay]}
    LayActions = {"controltype": "Layout", 'controlset': {"generalset":{"layoutformat": "double"}}, "columns": [eventDrop, ActionLayout , ]}
    ActionSection = {"controlset": {}, "controltype": "section", 'name': 'ActionSection', 'dir': 'Dir', 'columns': [lay.LayActions, ]}
    actionsectionrow = {"controltype": "section", 'sectionname': "ActionSection"}
    LayRepeat = {"controlset": {}, 'controltype': 'LayoutRepeat', "PrimaryNode": ".Actions", "columns": [lay.LayHeader, actionsectionrow], "addrowlay":lay.addrowlay}
    # Section example
    pt = {"controlset": {}, "PrimaryNode": ".Presentation", "TabName": "Presentation", "columns": [playout, ]}

    at = {"controlset": {}, "PrimaryNode": ".Action", "TabName": "Action", "columns": [LayRepeat]}

    layoutSettings = {"controlset": {}, "controltype": "TabGroup", "columns": [gt, pt, at]}
    layoutSettingsSection = {"controlset": {}, "controltype": "section", 'name': 'layoutSettingsSection', 'PrimaryNode': 'Config.ElementSettings','dir': 'Dir', 'columns': [layoutSettings, footerlayout, ]}
    # Form example
    layoutSettingsform = {"controlset": {}, "controltype": "form", 'name': 'layoutSettingsform', 'dir': 'Dir', 'sectionname': "layoutSettingsSection"}
    if type == "layoutSettingsSection":
        return layoutSettingsSection
    elif type == "layoutSettingsform":
        return layoutSettingsform
    elif type == "ActionSection":
        return ActionSection
    return ""
