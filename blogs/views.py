import random

from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.core.paginator import Paginator
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from .email import addsubscriber
from django.contrib import messages
       
def getyear():
    yr = datetime.now().year
    return yr
def HomepageView(request):

    if request.method == 'GET':
        context = {
            'posts': Post.objects.all().order_by('-date')[:5],
            'posts2':Post.objects.all().order_by('-date')[5:10],
            'year': getyear(),
            'message':'notsubscribed'
        }
        return render(request,'index.html',context)

    if request.method == 'POST':

        name= request.POST['name']
        email = request.POST['email']
        addsubscriber(name=name,email=email)
        if EmailModel.objects.all().filter(email__exact=email):
            message='already'
        else:
         emailmodel = EmailModel(name=name,email=email)
         emailmodel.save()
         message='success'
        context = {
            'posts': Post.objects.all().order_by('-date')[:5],
            'posts2': Post.objects.all().order_by('-date')[5:10],
            'year': getyear(),
            'message':message
        }
        return render(request, 'index.html', context)

class AllPostsView(View):
   def get(self,request):
       pages=[]
       posts = Post.objects.all().order_by('-date')
       titles = [p.title for p in posts]
       
       paginator = Paginator(posts, 9)

       page_num = request.GET.get('page')
       paginator.get_elided_page_range(2, on_each_side=1, on_ends=1)

       page_obj = paginator.get_page(page_num)

       for i in range(paginator.num_pages):
           pages.append(i + 1)
       if 'term' in request.GET:
           query = Post.objects.filter(title__contains = request.GET.get('term'))
           titles = list()
           for title in query:
               titles.append(title.title)
           return JsonResponse(titles,safe=False) 

       return render(request, 'all-posts.html', {'page_obj': page_obj, 'posts': posts,'pages':pages,'len_p':len(pages),'year':getyear()})

class DetailedPostView(View):
    def get(self,request,slug):
        stored_posts = request.session.get('stored_posts')
        post = Post.objects.get(slug=slug)
        posts = Post.objects.all().order_by('date')
        p = list(posts)
        posts= random.choices(p,k=3)
        form = CommentForm()
        rl = False

        if stored_posts != None:
         if post.id not in stored_posts:
            rl = False
         else:
            rl =True


        return render(request, 'single-post.html', {
            'post': post,
            'tags': post.tag.all(),
            'form':form,
            'comments':post.comments.all(),
            'rl':rl,
            'year':getyear(),
            'posts':posts
        })
    def post(self,request,slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        posts = Post.objects.all().order_by('date')
        p = list(posts)
        posts= random.choices(p,k=3)
        if form.is_valid():
            comment= form.save(commit=False)
            comment.post=post
            comment.save()
            return HttpResponseRedirect(reverse('specific_post',args=[slug]))

        return render(request, 'single-post.html', {
            'post': post,
            'tags': post.tag.all(),
            'form': form,
            'comments': post.comments.all(),
            'year':getyear(),
            'posts': posts
        })
class ReadLaterView(View):
    def get(self,request):
        stored_posts = request.session.get('stored_posts')
        context = {}
        if stored_posts is None:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context['posts'] = posts
            context['has_posts'] = True
        context['year'] = getyear()
        return render(request,'stored_posts.html',context)
    def post(self,request):
         stored_posts = request.session.get('stored_posts')
         if stored_posts is None:
             stored_posts = []
         post_id = int(request.POST['post_id'])
         if post_id not in stored_posts:
             stored_posts.append(post_id)

         else:
             stored_posts.remove(post_id)
         request.session['stored_posts'] = stored_posts

         return HttpResponseRedirect('/')

class SearchView(View):
        def post(self, request):
            searched = request.POST['search1']
            post = Post.objects.all().filter(title__contains=searched)

            return render(request, 'search_results.html', {
                'posts': post
            })

class ContactView(View):
    def get(self,request):
        return render(request,'contact.html',{
            'year':getyear()
        })
    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        contactmodel = ContactModel(name=name,email=email,message=msg)
        contactmodel.save()

        return render(request, 'contact.html', {
            'year': getyear()
        })
class AboutView(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        posts = Post.objects.all().order_by('date')
        p = list(posts)
        posts= random.choices(p,k=3)
        context = super().get_context_data()
        context['posts'] = posts
        context['year'] = getyear()
        
        return context

class Guestpostview(View):
    def get(self,request):
        form = Guestpostform(use_required_attribute=False)
        return render(request,'guestpost.html',{'form':form})
    def post(self,request):
        form = Guestpostform(request.POST)
        if form.is_valid():
         data = form.cleaned_data
         form.save()
         messages.success(request,'Thank you for contributing.\n If we find your blog helpful, we will publish and will send you the confirmation email.')
         return HttpResponseRedirect(reverse('gp'))
        else:
            messages.error(request, 'Fill out all the fields properly.')
            return HttpResponseRedirect(reverse('gp'))
def products(request):
    year = getyear()
    return render(request,'products.html',{'year':year})
def tandc(request):
    year = getyear()
    return render(request,'termsandconditions.html',{'year':year})
def pp(request):
    year = getyear()
    return render(request,'pp.html',{'year':year})
def page_not_found_view(request,exception):
    return render(request,'404.html',status=404)

