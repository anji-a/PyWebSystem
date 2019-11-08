from bs4 import BeautifulSoup
from bs4 import Comment
import json


def parsehtmltodict(html=""):
    sourceDict = {}
    sourceDict["name"] = "Sample"
    sourceDict["dir"] = "Dir"
    sourceDict["elements"] = []
    soup = BeautifulSoup(html, 'lxml')
    #print(" --- ", soup.find(attrs={"id": "sample"}).find(attrs={"data-parse": "flase"}))
    taglist = soup.find(attrs={"id": "sample"}).find(attrs={"data-parse": "true"})
    if taglist is None:
        taglist = []
    layoutelemt = []
    for index, tag in enumerate(taglist.contents):
        #print(tag, "\n.......")
        if not(isinstance(tag, Comment)) and tag != "\n" and tag.attrs != {}:
            #print(tag.attrs)
            if tag.has_attr("data-element"):
                if tag.attrs.get("data-element", "") == "Layout":
                    layele = looplayout(tag)
                    layoutelemt.append(layele)

    sourceDict["elements"] =layoutelemt
    return sourceDict


def looplayout(tag):
    #print(tag)
    layout = {}
    dataset = tag.attrs.get("data-set", "{}")
    datasetdict = json.loads(dataset)
    layout["controlset"] = datasetdict
    layout["controltype"] = tag.attrs.get("data-cell", "")
    layout["columns"] = []
    columnlist = []
    for key, ctag in enumerate(tag.contents):
        # print(ctag)
        if not (isinstance(tag, Comment)) and tag != "\n" and tag.attrs != {}:
            if tag.has_attr("data-element"):
                if ctag.attrs.get("data-type", "") == "Column":
                    col = loopcolumn(ctag)
                    columnlist.append(col)
                if ctag.attrs.get("data-type", "") == "ColumnLayout":
                    #print(ctag.find(attrs={'data-element': 'Layout'}))
                    lay = looplayout(ctag.find(attrs={'data-element': 'Layout'}))
                    columnlist.append(lay)
    layout["columns"].extend(columnlist)
    return layout


def loopcolumn(tag):
    #print(tag)
    column = {}
    dataset = tag.attrs.get("data-set", "{}")
    datasetdict = json.loads(dataset)
    column["controlset"] = datasetdict
    column["controltype"] = tag.attrs.get("data-cell", "")
    return column
