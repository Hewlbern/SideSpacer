from django.contrib import admin
from Spaces.models import Category, Page

class PageAdmin(admin.ModelAdmin):
#category title and URL from model
    list_display = ('title', 'category','url')



# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'slug','likes')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
