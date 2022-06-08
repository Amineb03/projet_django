from unicodedata import name
from django.conf.urls import urls
from django.contrib.auth.views import LoginView

urlpatterns = [

    urls(r'login/$', view = LoginView.as_view(template_name="account/login.html"), name="login")
]