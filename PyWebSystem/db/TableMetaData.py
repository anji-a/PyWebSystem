
# need to implement to get data from DB
def get_metadata_class(cls):

    if cls == "element":
        return {"columns": ["PyName", "PyCreateDate", "PyUpdateDate", "PyStream", "PyKey", "PyClass", "PyDir"], "primarykey": ["PyKey"], "tableName": "py_element"}
