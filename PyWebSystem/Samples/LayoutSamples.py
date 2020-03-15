import PyWebSystem.Samples.columnsexamples as sam

ActionLay = {"controltype": "Layout", 'controlset': {"generalset":{"layoutformat": "double"}}, "columns": [sam.inlinestyle, sam.customcss]}
LayHeader = {"controltype": "Layout", "columns": [sam.Label, ]}
RunMethodLay = {"controltype": "Layout", 'controlset': {"generalset": {"layoutformat": "", "Condition": ".Action=='1'"}}, "columns": [sam.methodname, ]}
OpenModelwindowLay = {"controltype": "Layout", 'controlset': {"generalset": {"layoutformat": "", "Condition": ".Action=='2'"}}, "columns": [sam.modelname, ]}
ActionLayout = {"controltype": "Layout", "columns": [sam.actionDrop, OpenModelwindowLay, RunMethodLay]}
eventlay = {"controltype": "Layout", "columns": [sam.eventDrop, sam.deleteicon]}
LayActions = {"controltype": "Layout", 'controlset': {"generalset": {"layoutformat": "double"}, "presentationset": {"css": "w3-border"}}, "columns": [eventlay, ActionLayout , ]}
addrowlay = {"controltype": "Layout", "columns": [sam.addicon, ]}

