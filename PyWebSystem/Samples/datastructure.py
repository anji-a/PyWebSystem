# Config.ElementSettings.Action.Actions[0].Params


Config = {"type": "dict", "childes": ["ElementSettings"]}

ElementSettings = {"type": "dict", "childes": ["General", "Presentation", "Action"]}

General = {"type": "dict", "childes": ["containerformat"]}

Presentation = {"type": "dict", "childes": ["flot"]}

Action = {"type": "dict", "childes": ["Actions"]}

Actions = {"type": "list", "childes": ["actiontype"]}

actiontype = {"type": "dict", "childes": ["Event", "Params"]}

Params = {"type": "list", "childes": ["parameter"]}

parameter = {"type": "dict", "childes": ["name", "value"]}


datast = {"config": Config, "ElementSettings": ElementSettings, "General": General, "Presentation": Presentation,
          "Action": Action, "Actions": Actions, "actiontype": actiontype, "Params": Params, "parameter": parameter}