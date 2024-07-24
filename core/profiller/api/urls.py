from django.urls import path
from profiller.api.views import ProfilViewSet, ProfilList

"""
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """

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
