
from django.urls import path
from . import views

urlpatterns = [
   path('chai',views.all_chai,name='chai')
]
