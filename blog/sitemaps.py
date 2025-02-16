from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Blog
from tools.models import Tools 

class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Blog.objects.filter(status='published')
    
    def lastmod(self, obj):
        return obj.modified_at
    
class StaticSitemap(Sitemap):
    priority = 0.5
    changefreq = "monthly"

    def items(self):
        return ['home', 'about', 'contact']
    
    def location(self, item):
        return reverse(item)
    
class ToolsSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Tools.objects.filter(status='published')
    
    def lastmod(self, obj):
        return obj.modified_at