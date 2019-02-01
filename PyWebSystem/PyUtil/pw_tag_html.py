from bs4 import BeautifulSoup

def pw_prepare_input(item={}, soup=None, *args, **kwargs):
    # {actiontype:Link, action_name:SampleLink, action_data:{[{"event":"click","eventdata":[{"action":"Close"}]}]}}
    sampledata = {"actiontype": "input", "property_name": ".Name", "label": "Enter Name", "Placeholder":"Enter Name",
                  "presentation": {},  "action_data": {[{"event": "click", "eventdata": [{"action": "Close"}]}]}}
    div_tag = soup.new_tag()
