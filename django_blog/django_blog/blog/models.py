from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from accounts.models import Author


class Post(models.Model):
    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    id = models.AutoField(unique=True, primary_key=True, null=False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    category = models.CharField(max_length=50, null=False, blank=False, default='no category')
    created_at = models.DateTimeField(auto_now=True)
    #published_at = models.DateTimeField(auto_now=True)
    #updated_at = models.DateTimeField()   
 
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class PostCategory(models.Model):
    class Meta:
        db_table = "post_categories"
        verbose_name = _('PostCategory')
        verbose_name_plural = _('PostCategories')

    id = models.AutoField(unique=True, null=False, primary_key=True)
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Comment(models.Model):
    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    id = models.AutoField(unique=True, primary_key=True, null=False)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
    #user_id = models.ForeignKey('auth.User', default = User.id, on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField(null=False, blank=False)
 
    def __str__(self):
        return self.title