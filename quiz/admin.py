from django.contrib import admin
from quiz.models import *

class DatoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Dato, DatoAdmin)
