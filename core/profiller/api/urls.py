from django.urls import path, include
from profiller.api.views import ProfilViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user-profiles', ProfilViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



""" First Version

profil_list = ProfilList.as_view()
profil_detay = ProfilViewSet.as_view(
    {'get': 'retrieve',
     'delete': 'destroy',
     'put': 'update',
     })

urlpatterns = [
    path('user-profiles/', profil_list, name='profiles'),
    path('user-profiles/<int:pk>', profil_detay, name='profile-detay')
]

"""