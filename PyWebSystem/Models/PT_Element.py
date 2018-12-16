from django.db import models


# Create your models here.
class PTElement(models.Model):
    element_name = models.CharField(max_length=50, unique=True)
    element_createddatetime = models.DateTimeField()
    element_updatedatetime = models.DateTimeField()
    element_stream = models.TextField(blank=True, null=True)
    element_type = models.CharField(max_length=50)
    element_mode = models.CharField(max_length=50)
    element_displayname = models.CharField(max_length=50)
    element_dir = models.CharField(max_length=100)

    def set_data(self, data):
        self.element_name = data.get('element_name', '')
        self.element_createddatetime = data.get('element_createddatetime', '')
        self.element_updatedatetime = data.get('element_updatedatetime', '')
        self.element_stream = data.get('element_stream', '')
        self.element_type = data.get('element_type', '')
        self.element_displayname = data.get('element_displayname', '')
        self.element_mode = data.get('element_mode', '')
        self.element_dir = data.get('element_dir', '')
        # print(json.dumps(data))
        #self.py_stream = base64.b64encode(json.dumps(data).encode('utf-8'))

    def get_data(self):
        #return json.loads(base64.b64decode(self.py_stream).decode('utf-8'))
        return self.element_stream
