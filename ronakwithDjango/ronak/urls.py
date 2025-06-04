from django.urls import path
from . import views

urlpatterns = [
      path('', views.all_ronak, name='all_home'),  #localhost:8000/ronak
      path('<int:ronak_id>/', views.ronak_detail, name='ronak_detail'),  #localhost:8000/ronak/1
      path('ronak_stores/', views.ronak_store_view, name='ronak_stores'),  #localhost:8000/ronak/ronak_stores
]