savebutton = {"controltype": "button", "Label": "Save", "onclick": "processeventaction(event)", "controlset": '{"actionset": [{"event": "click", "eventdata": [{"action": "exeaction", "actionname": "resetsettings_for_element", "Actiontype":"SaveSettings"}]}]}'}
event = {"1": "Click", "2": "Hover", "3": "Double Click", "4": "Right Click1"}
actions = {"1": "Run Method", "2": "Open Model Window", "3": "Close"}
eventDrop = {'controlset': {}, 'controltype': 'select', 'property': '.Event',
             'sourcelist': event, "Label": "Select Event"}
actionDrop = {'controlset': '{"actionset": [{"event": "change", "eventdata": [{"action": "refreshsection"}]}]}',
              'controltype': 'select', 'property': '.Action',
              'sourcelist': actions, "Label": "Select Action"}
event = {"1": "Click", "2": "Hover", "3": "Double Click", "4": "Right Click"}
actions = {"1": "Run Method", "2": "Open Model Window", "3": "Close"}
Label = {"controlset": {}, "controltype": "Label", "labelstart": "Action ", "property": ".index"}
inlinestyle = {"controlset": {}, "controltype": "Input", "Label": "Inline Style", "property": ".style"}
customcss = {"controlset": {}, "controltype": "Input", "Label": "Custom CSS", "property": ".css"}

methodname = {"controlset": {}, "controltype": "Input", "Label": "Select Method", "property": ".method"}
modelname = {"controlset": {}, "controltype": "Input", "Label": "Select Model", "property": ".model"}
deleteicon = {"controlset": '{"actionset": [{"event": "click", "eventdata": [{"action": "deleterow"}, {"action": "refreshothersection","sectioname":"layoutSettingsSection"}]}]}', "controltype": "icon", "iconcss": "fa fa-trash fa-lg"}
addicon = {"controlset": '{"actionset": [{"event": "click", "eventdata": [{"action": "addrow"},{"action": "refreshothersection","sectioname":"layoutSettingsSection"}]}]}', "controltype": "icon", "iconcss": "fa fa-plus fa-lg"}