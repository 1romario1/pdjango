
from . import views 
from django.urls import include, path

urlpatterns = [
    path('lista/',views.aprendizlist,name="aprendizlist.html"),
]