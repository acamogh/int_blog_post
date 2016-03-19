from django.contrib import admin

from .models import Post,Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','description']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Post

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
