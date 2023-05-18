from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField( max_length=50)
    image = models.ImageField( upload_to="post/")
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    RATING = (
        ("1",'1'),
        ("2",'2'),
        ("3",'3'),
        ("4",'4'),
        ("5",'5'),
        ("6",'6'),
        ("7",'7'),
        ("8",'8'),
        ("9",'9'),
        ("10",'10'),
    )
    rating = models.CharField(max_length=50 , choices=RATING)
    slug = models.SlugField()
    STATUS = (
        ('Published',"published"),
        ('Draft',"draft"),
    )
    status = models.CharField(max_length=50 , choices=STATUS , default="published")
    category = models.ManyToManyField(Category , blank=True)
    likes = models.ManyToManyField(User , related_name='posts_like' , blank=True)
    
    
    def __str__(self):
        return self.title
    
    
class CommentPost(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='comment')
    user = models.ForeignKey(User , related_name='comment_user' , on_delete=models.CASCADE)
    content = models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=True)
    
    def __str__(self):
        return (f'{self.user} - post : {self.post}')
    class Meta:
        ordering = ('created',)