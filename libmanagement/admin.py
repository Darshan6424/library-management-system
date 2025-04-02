from django.contrib import admin
from libmanagement.models import Student, Book, BookLend
# Register your models here.

admin.site.register(Student)
admin.site.register(Book)
admin.site.register(BookLend)

