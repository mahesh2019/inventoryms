from django.conf.urls import url
from .views import *
from django.contrib import admin


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^(?P<pk>\d+)$', detail, name="detail"),
    url(r'^edit/(?P<pk>\d+)$', edit, name="edit"),
    url(r'^addnew$', addnew, name="addnew"),
    url(r'^admin/', admin.site.urls),

]