from django.urls import path
from . import views

urlpatterns = [
      path('', views.all_ronak, name='all_home'),  #localhost:8000/ronak
]