from django.contrib import admin
from .models import Post, Book, Filter

# Register your models here.

# domuko55@gmail.com
admin.site.register(Filter)
admin.site.register(Post)
admin.site.register(Book)
