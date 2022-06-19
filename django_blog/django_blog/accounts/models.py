from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):     
    is_reader = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
    class Meta():
        db_table = "Users"
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username


class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    country = models.CharField(max_length=50)

    class Meta():
        db_table = "Readers"
        verbose_name = _('Reader')
        verbose_name_plural = _('Readers')

    def __str__(self):
      return self.country


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    activity = models.CharField(max_length=50)
    company = models.CharField(max_length=50) 

    class Meta():
        db_table = "Authors"
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    def __str__(self):
        return self.activity


#class AuthorCategory(models.Model):
#    class Meta:
#        db_table = "author_categories"
#        verbose_name = _('AuthorCategory')
#        verbose_name_plural = _('AuthorCategories')
#
#    id = models.AutoField(primary_key=True)
#    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
#    author_id = models.OneToOneField('Author', on_delete=models.CASCADE)
#    
#    def __str__(self):
#        return self.name


#class Subscription(models.Model):
#    class Meta:
#        db_table = "subscriptions"
#        verbose_name = _('Subscription')
#        verbose_name_plural = _('Subscriptions')

#    id = models.AutoField(primary_key=True)
#    subscriber_user_id = models.OneToOneField('User', on_delete=models.CASCADE)
    #subscription_user_id = models.ForeignKey('User', on_delete=models.CASCADE)
#    subscribed_at = models.DateTimeField(auto_now=True)
#    
#    def __str__(self):
#        return self.id