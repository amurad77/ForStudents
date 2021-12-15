from django.contrib import admin

# Register your models here.

from core.models import University_left, University_right, Book, Project, Contact

admin.site.register([University_left, University_right, Book, Project, Contact])