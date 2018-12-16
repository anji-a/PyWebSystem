from bs4 import Tag, SoupStrainer


def find_child_codes(tag=None, attrs={}):
    results = []
    #print(tag.attrs)
    if isinstance(tag, Tag):
        for sibling in tag.contents:
            # print(sibling)
            if sibling != "\n" and sibling.attrs != {}:
                for attr, match_against in list(attrs.items()):
                    # print(attr,match_against)
                    attr_value = sibling.get(attr, "")
                    """if attr_value == match_against:
                        results.append(sibling)"""
                    strainer = SoupStrainer(None, attrs, None)
                    if strainer._matches(attr_value, match_against):
                        results.append(sibling)
    return results
