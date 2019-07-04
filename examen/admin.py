from django.contrib import admin
from . models import usuario, examenes, servicios

admin.site.register(usuario)
admin.site.register(examenes)
admin.site.register(servicios)

