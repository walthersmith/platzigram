"""Users Models."""

#Django
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """ profile Model
    Proxi model that extends the base data with other 
    information"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20,blank=True)

    picture = models.ImageField(upload_to='users/pictures',blank=True,null=True)

    follow = models.ManyToManyField(User,related_name='follow')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    @property
    def total_follows(self):
        """
            Likes for the post
            :return Integer: likes for the post
        """
        return self.follow.count()


    def __str__(self):
        """return Username"""
        return self.user.username



