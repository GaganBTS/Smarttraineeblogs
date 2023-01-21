from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    class Media:
        js = ('tiny.js',)



admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(CommentModel)
admin.site.register(EmailModel)
admin.site.register(ContactModel)
admin.site.register(Guestpost)
