from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Post

class StaticViewsSitemap(Sitemap):
    changefreq='always'
    def items(self):
        return ['about','contact','home','all_posts','read-later','pp','tc','products','search']
    def location(self, item):
        return reverse(item)

class PostSitemap(Sitemap):
    changefreq = 'always'
    def items(self):
        return Post.objects.all()