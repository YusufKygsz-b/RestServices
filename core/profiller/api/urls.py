from django.urls import path
from profiller.api import views

urlpatterns = [
    path('user-profiles/', views.ProfilList.as_view(), name='profiles')
]
