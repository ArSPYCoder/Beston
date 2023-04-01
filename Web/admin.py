from django.contrib import admin
from .models import Expense, Incom, Token
# Register your models here.

admin.site.register(Expense)
admin.site.register(Incom)
admin.site.register(Token)
