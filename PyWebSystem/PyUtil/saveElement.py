from faker import Faker
fakegen = Faker()
from PyWebSystem.Models.PY_Element import PYElement


def saveElement(context={}, action={}, *args, **kwargs):
    print("hi", action)
    print(context)
    data = {}
    data['element_name'] = fakegen.name()
    data['element_createddatetime'] = fakegen.date()
    data['element_updatedatetime'] = fakegen.date()
    # data['element_stream'] = fakegen.text()
    data['element_mode'] = 'Section'
    # print(str.encode(str(data)))
    pyObject = PYElement()
    print(pyObject.__dict__)
    #pyObject.set_data(data=data)

    #pyObject.save()
