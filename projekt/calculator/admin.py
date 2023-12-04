from django.contrib import admin
from calculator.models import Note, User

# Register your models here.
admin.site.register(User)
admin.site.register(Note)