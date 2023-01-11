from django.urls import path
from .views import *

urlpatterns = [
    path('',HomepageView,name='home'),
    path('posts',AllPostsView.as_view(),name='all_posts'),
    path('posts/<slug:slug>',DetailedPostView.as_view(),name='specific_post'),
    path('read-later',ReadLaterView.as_view(),name='read-later'),
    path('search-results',SearchView.as_view(),name='search'),
    path('contact',ContactView.as_view(),name='contact'),
    path('about',AboutView.as_view(),name='about'),
    path('products',products,name='products'),
    path('terms-and-conditions',tandc,name='tc'),
    path('privacy-policy',pp,name='pp'),

    
]