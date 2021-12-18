from django.contrib import admin

# Register your models here.

from core.models import University, Book, Project, Contact, Meqsed, Pdf

admin.site.register([University, Book, Project, Contact, Meqsed, Pdf])