from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from PyWebSystem.HtmlParse.ParseCSS import parseCSS


class StartupMiddleware(MiddlewareMixin):
    def sample(self):
        print("Hello world")


print("hello")
parseCSS()