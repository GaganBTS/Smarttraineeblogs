
from django.db import models
from django.core.validators import EmailValidator
from django.shortcuts import reverse


# Create your models here.
class Author(models.Model):
    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80,validators=[EmailValidator])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Post(models.Model):
    title = models.CharField(max_length=70,null=False)
    excerpt = models.TextField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=False)
    image = models.URLField(null=True)
    slug = models.SlugField(unique=True,db_index=True)
    date = models.DateField(auto_now=True)
    tag = models.ManyToManyField('Tag')
    content = models.TextField()

    def __str__(self):
        return f'{self.title}'
    def get_absolute_url(self):
        return reverse('specific_post',args=[self.slug])

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.caption}'

class CommentModel(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField(max_length=500)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return f'{self.user_name}'

class EmailModel(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=80,validators=[EmailValidator])
    def __str__(self):
        return f'{self.email}'
    
    
class ContactModel(models.Model):
     name = models.CharField(max_length=80)
     email = models.EmailField(max_length=80,validators=[EmailValidator])
     message = models.TextField()
     def __str__(self):
        return f'{self.name}{self.email}'