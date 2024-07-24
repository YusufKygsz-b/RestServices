from django.contrib import admin

# Register your models here.

from profiller.models import Profil, ProfilState

admin.site.register(Profil)
admin.site.register(ProfilState)