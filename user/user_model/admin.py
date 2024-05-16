from django.contrib import admin
from .models import User, Account, Address, Fullname
# Register your models here.
admin.site.register(Fullname)
admin.site.register(Account)
admin.site.register(Address)
admin.site.register(User)
