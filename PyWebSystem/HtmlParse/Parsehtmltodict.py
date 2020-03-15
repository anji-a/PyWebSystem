from bs4 import BeautifulSoup
from bs4 import Comment
import json
from datetime import datetime
from PyWebSystem.PyUtil.pw_logger import logmessage


def parsehtmltodict(html=""):
    logmessage("parsehtmltodict", "warning", )
    soup = BeautifulSoup(html, 'lxml')
    # logmessage("parsehtmltodict", "warning", soup)
    htmltag = soup.find(attrs={"data-html": "true"})
    sourceDict = {}
    sourceDict["ElementName"] = htmltag.attrs.get("data-elementname", "")
    sourceDict["name"] = htmltag.attrs.get("data-elementname", "")
    sourceDict["CreateDate"] = datetime.now().isoformat(timespec='microseconds')
    sourceDict["Updatedate"] = datetime.now().isoformat(timespec='microseconds')
    sourceDict["Dir"] = htmltag.attrs.get("data-Dir", "")
    sourceDict["DirVerion"] = htmltag.attrs.get("data-DirVerion", "")
    sourceDict["ElementType"] = htmltag.attrs.get("data-controltype", "")
    sourceDict["controltype"] = htmltag.attrs.get("data-controltype", "")
    sourceDict["elementclass"] = htmltag.attrs.get("data-elementclass", "")
    sourceDict["columns"] = []
    sourceDict["controlset"] = {}

    sourceDict["Html"] = "".join([line.strip("\n\t") for line in soup.find(attrs={"data-parse": "true"}).prettify()])
    #print(" --- ", soup.find(attrs={"id": "sample"}).find(attrs={"data-parse": "flase"}))
    taglist = soup.find(attrs={"data-parse": "true"})
    if taglist is None:
        taglist = []
    layoutelemt = []
    for index, tag in enumerate(taglist.contents):
        #print(tag, "\n.......")
        if not(isinstance(tag, Comment)) and tag != "\n" and tag.attrs != {}:
            #print(tag.attrs)
            if tag.has_attr("data-element"):
                if tag.attrs.get("data-element", "") == "LayoutGroup":
                    layele = looplayout(tag)
                    layoutelemt.append(layele)
                elif tag.attrs.get("data-element", "") == "section":
                    layele = addsection(tag)
                    layoutelemt.append(layele)
                elif tag.attrs.get("data-element", "") == "SectionGroup":
                    layele = loopsection(tag)
                    layoutelemt.append(layele)
                elif tag.attrs.get("data-element", "") == "RepeatSection":
                    layele = loopsection(tag)
                    layoutelemt.append(layele)
                elif tag.attrs.get("data-element", "") == "RepeatTable":
                    layele = looplayout(tag)
                    layoutelemt.append(layele)
    sourceDict["columns"] =layoutelemt
    return sourceDict


def addsection(tag):
    #print(tag)
    section = {}
    dataset = tag.attrs.get("data-set", "{}")
    datasetdict = json.loads(dataset)
    section["controlset"] = datasetdict
    section["controltype"] = tag.attrs.get("data-cell", "")
    section["sectionname"] = tag.attrs.get("data-name", "")
    return section


def loopsection(tag):
    layout = {}
    dataset = tag.attrs.get("data-set", "{}")
    datasetdict = json.loads(dataset)
    layout["controlset"] = datasetdict
    layout["controltype"] = tag.attrs.get("data-cell", "")
    layout["columns"] = []
    columnlist = []
    for key, ctag in enumerate(tag.div.contents):
        # print(ctag)
        if not (isinstance(tag, Comment)) and tag != "\n" and tag.attrs != {}:
            if tag.has_attr("data-element"):
                if ctag.attrs.get("data-type", "") == "SectionColumn":
                    col = addsection(ctag)
                    columnlist.append(col)
    layout["columns"].extend(columnlist)
    return layout


def looplayout(tag):
    # print("parent tage:\n", tag, "\n")
    layout = {}
    dataset = tag.attrs.get("data-set", "{}")
    datasetdict = json.loads(dataset)
    layout["controlset"] = datasetdict
    layout["controltype"] = tag.attrs.get("data-cell", "")
    layout["columns"] = []
    columnlist = []
    # logmessage("parsetodict", "warning", tag.div)
    for key, ctag in enumerate(tag.div.contents):
        # print(ctag, "\n")
        if not (isinstance(tag, Comment)) and tag != "\n" and tag.attrs != {}:
            if tag.has_attr("data-element"):
                if ctag.attrs.get("data-type", "") == "Column":
                    col = loopcolumn(ctag)
                    columnlist.append(col)
                elif ctag.attrs.get("data-type", "") == "SectionColumn":
                    col = addsection(ctag)
                    columnlist.append(col)
                elif ctag.attrs.get("data-type", "") == "ColumnLayout":
                    #print(ctag.find(attrs={'data-element': 'Layout'}))
                    lay = looplayout(ctag.find(attrs={'data-element': 'LayoutGroup'}))
                    columnlist.append(lay)
                elif ctag.attrs.get("data-type", "") == "SectionGroup":
                    #print(ctag.find(attrs={'data-element': 'Layout'}))
                    lay = loopsection(ctag.find(attrs={'data-element': 'SectionGroup'}))
                    columnlist.append(lay)
                elif ctag.attrs.get("data-type", "") == "ButtonBar":
                    lay = looplayout(ctag.find(attrs={'data-element': 'ButtonBar'}))
                    columnlist.append(lay)
    layout["columns"].extend(columnlist)
    return layout


def loopcolumn(tag):
    #print(tag)
    column = {}
    dataset = tag.attrs.get("data-set", "{}")
    datasetdict = json.loads(dataset)
    # {'controlset': {}, 'controltype': 'select', 'property': '.containerformat','sourcelist': containerformat, "Label": "Container Format"}
    # {'controlset': {}, 'controltype': 'radio', 'property': '.deferload', 'sourcelist': deferload}
    # {"controlset": {}, "controltype": "Input", "Label": "Inline Style", "property": ".style"}
    column["controlset"] = datasetdict
    column["controltype"] = tag.attrs.get("data-cell", "")
    column["property"] = datasetdict.get("General", {}).get("property", "")
    column["sourcelist"] = datasetdict.get("General", {}).get("sourcelist", "")
    column["Label"] = datasetdict.get("General", {}).get("Label", "")
    return column
