from bs4 import BeautifulSoup
from PyWebSystem.PyUtil.pw_extra_methods import id_generator
from PyWebSystem.PyUtil.DickUpdate import list_loop


def pw_navigation(context={}, *args, **kwargs):
    # need navigation element name to load data
    sample_data = {"name": "Sample", "settings": {"MobileUse": "Yes"}, "action_items": [
        {"actiontype": "Link", "actionname": "SampleLink", "action_data": {}},
        {"actiontype": "Button", "actionname": "SampleButton", "action_data": {}},
    ]}
    html = ""
    soup = BeautifulSoup(html, "lxml")
    nav_tag = soup.new_tag("nav")
    nav_tag["class"] = "navbar navbar-expand-lg navbar-light bg-light p-0"
    container_tag = soup.new_tag("div")
    container_tag["class"] = "container-fluid"
    toggle_id = id_generator(prefix="nav")
    sample_data["toggle_id"] = toggle_id
    container_tag.append(pw_prepare_header(sample_data, soup))
    item_div_tag = soup.new_tag("div")
    item_div_tag["class"] = "collapse navbar-collapse"
    item_div_tag["id"] = toggle_id
    item_ul_tag = soup.new_tag("ul")
    item_ul_tag["class"] = "navbar-nav mr-auto"
    for key, item, path in list_loop(sample_data.get("action_items", [])):
        item_ul_tag.append(pw_prepare_item(key, item, soup))
    item_div_tag.append(item_ul_tag)
    container_tag.append(item_div_tag)
    nav_tag.append(container_tag)
    print(str(nav_tag), "\n////////////")
    soup.append(nav_tag)
    return str(soup)


def pw_prepare_item(key="", item={}, soup=None):
    action_type = item.get("actiontype", "")
    if action_type is "Link":
        return pw_prepare_link(item, soup)
    elif action_type is "Button":
        return pw_prepare_button(item, soup)


def pw_prepare_link(item={}, soup=None):
    li_tag = soup.new_tag("li")
    li_tag["class"] = "nav-item"
    a_tag = soup.new_tag("a")
    a_tag["class"] = "nav-link"
    a_tag.string = item.get("actionname", "")
    li_tag.append(a_tag)
    return li_tag


def pw_prepare_button(item={}, soup=None):
    li_tag = soup.new_tag("li")
    li_tag["class"] = "nav-item"
    button_tag = soup.new_tag("button")
    button_tag["class"] = "nav-button"
    button_tag.string = item.get("actionname", "")
    li_tag.append(button_tag)
    return li_tag


def pw_prepare_header(sample_data={}, soup=None):
    header_div_tag = soup.new_tag("div")
    header_div_tag["class"] = "navbar-header"
    button_tag = soup.new_tag("button")
    button_tag["type"] = "button"
    button_tag["class"] = "navbar-toggler"
    button_tag["data-toggle"] = "collapse"
    button_tag["data-target"] = '#'+sample_data.get("toggle_id", "")
    button_tag["aria-expanded"] = "false"
    span_sr_tag = soup.new_tag("span")
    span_sr_tag["class"] = "sr-only"
    span_sr_tag.string = "Toggle navigation"
    button_tag.append(span_sr_tag)
    for i in range(3):
        span = soup.new_tag("span")
        span["class"] = "icon-bar"
        button_tag.append(span)
    header_div_tag.append(button_tag)
    return header_div_tag


def pw_prepare_input(item={}, soup=None, *args, **kwargs):
    pass
