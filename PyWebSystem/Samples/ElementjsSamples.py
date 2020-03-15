from PyWebSystem.Samples.layoutSettings import layoutSettings

def gettablayoutsample():
    sourceDict = {}
    ## Need to make adjustments in Section Sample ##
    SectionSample = {'name': 'Sample', 'dir': 'Dir', 'elements': [{'controlset': {'gt': {'layouttype': 'Single', 'visibility': 'Always'}, 'pt': {}, 'at': {}},
                                                               'controltype': 'Layout', 'columns': [{'controlset': {}, 'controltype': 'Input'}]}]}
    ## List examples
    staticlist = {"Male": "Male", "Female": "Female"}

    ## Basic elements
    inputcol = {"controlset": {}, "controltype": "Input",  "Label": "EnterName:", "property": ".age"}
    checkboxcol = {'controlset': {}, 'controltype': 'checkbox', 'property': '.Sex', 'sourcelist': staticlist, "Label": "Select Sex"}
    radiocol = {'controlset': {}, 'controltype': 'radio', 'property': '.Gender', 'sourcelist': staticlist, "Label": "SelectGender:"}
    dropdowncol = {'controlset': {}, 'controltype': 'select', 'property': '.Gen', 'sourcelist': staticlist, "Label": "SelectItem:"}

    ## Layout samples
    LaySample = {"controltype": "Layout", "columns": [inputcol, checkboxcol, radiocol, dropdowncol]}
    dynamictab = {"controlset": {}, 'controltype': 'TabGroup', "TabType": "Dynamic", "TabName": ".Name", "TabNode": "Standard", "columns": [LaySample,]}
    Tabsample = {"controlset": {}, "controltype": "TabGroup", "PrimaryNode": ".Sample", "columns": [{"controlset": {}, "PrimaryNode": ".General", "TabName": "General", "columns": [LaySample,]},
                                                                       {"controlset": {}, "TabName": "Presentation", "tabstatus":"active", "columns": [LaySample,]},
                                                                       {"controlset": {}, "TabName": "Actions", "columns": [LaySample, dynamictab]},
                                                                        ]}

    layoutSetting = layoutSettings("layoutSettingsform")
    sourceDict["elements"] = [layoutSetting]
    return sourceDict
