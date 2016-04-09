from django.conf.urls import url
from . import views
#importuj funkcję url 
#zaimportuj lokalną biblioteke views 
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
     url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
#r=wyrazenie regularne, ^=ma się zaczynać, $=ma się kończyć, więc ma byc puste, czyli pusta jest część ścieżki po adresie komputera