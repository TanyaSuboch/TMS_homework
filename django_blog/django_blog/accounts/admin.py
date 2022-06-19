from django.contrib import admin
from .models import User, Reader, Author

# Register your models here.
admin.site.register(User)
admin.site.register(Reader)
admin.site.register(Author)
#admin.site.register(AuthorCategory)
#admin.site.register(Subscription)