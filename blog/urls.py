from django.conf.urls import url
from . import views
#importuj funkcję url 
#zaimportuj lokalną biblioteke views 
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
#r=wyrazenie regularne, ^=ma się zaczynać, $=ma się kończyć, więc ma byc puste, czyli pusta jest część ścieżki po adresie komputera