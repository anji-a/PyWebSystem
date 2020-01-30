

def gettablayoutsample():
    sourceDict = {}
    ## Need to make adjustments in Section Sample ##
    SectionSample = {'name': 'Sample', 'dir': 'Dir', 'elements': [{'controlset': {'gt': {'layouttype': 'Single', 'visibility': 'Always'}, 'pt': {}, 'at': {}},
                                                               'controltype': 'Layout', 'columns': [{'controlset': {}, 'controltype': 'Input'}]}]}
    inputcol = {'controlset': {}, 'controltype': 'Input'}
    checkboxcol = {'controlset': {}, 'controltype': 'checkbox'}
    radiocol = {'controlset': {}, 'controltype': 'radio'}
    dropdowncol = {'controlset': {}, 'controltype': 'select'}

    LaySample = {'controltype': 'Layout', 'columns': []}

    Tabsample = {"controlset": {}, "controltype": "TabGroup", "PrimaryNode": "", "columns": [{"controlset": {}, "TabName": "General", "columns": [LaySample,]},
                                                                       {"controlset": {}, "TabName": "Presentation", "columns": [{}]},
                                                                       {"controlset": {}, "TabName": "Actions", "columns": [{}]}]}
    sourceDict["elements"] = [Tabsample]
    return sourceDict
