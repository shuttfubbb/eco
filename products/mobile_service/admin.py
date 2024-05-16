from django.contrib import admin
from .models import Type, Producer, Mobile
# Register your models here.
admin.site.register(Mobile)
admin.site.register(Producer)
admin.site.register(Type)