from django.contrib import admin
from .models import Blog, Category

from ckeditor.widgets import CKEditorWidget
from django import forms
# Register your models here.

admin.site.register(Category)


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
        fields = '__all__'
    

class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = ['title', 'category', 'status', 'created_at']

admin.site.register(Blog, BlogAdmin) 
