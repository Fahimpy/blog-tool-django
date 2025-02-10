from django.db import models
from django.utils.text import slugify 
from ckeditor.fields import RichTextField
# Create your models here.

class Tools(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='tools/', blank=True, null=True)
    intro = RichTextField('Content', config_name='default', blank=True, null=True)
    custom_body_html = models.TextField(blank=True, null=True, help_text="Add custom HTML/Javascript for header")
    custom_footer_html = models.TextField(blank=True, null=True, help_text="Add custom CSS/Javascript for footer")
    content = RichTextField('Content', config_name='default', blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    index = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published'),], default='draft')

    def __str__(self):
        return self.name