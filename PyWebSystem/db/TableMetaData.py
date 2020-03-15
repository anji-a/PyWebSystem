#from PyWebSystem.customtags.pw_findelement import findelement
#from PyWebSystem.customtags.pw_findelement import findelement


def get_metadata_class(conext, cls):# need to implement to get data from DB
    if cls == "element":
        return {"columns": ["ElementName", "CreateDate", "Updatedate", "Html", "Json", "ElementType", "Dir", "DirVerion", "ElementKey","elementclass"], "primarykey": ["ElementKey"], "tableName": "element"}
    else:
        #return findelement(conext, ElementName=cls)
        return {}
