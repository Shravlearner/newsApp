from django.contrib import admin

# Register your models here.
from .models import Search, Article

admin.site.register(Search)
admin.site.register(Article)