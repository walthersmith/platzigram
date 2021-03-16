""" Post Models"""

#Django
from django.db import models 
from django.contrib.auth.models import User 

class Post(models.Model):
    """Post model."""

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile',on_delete=models.CASCADE)
    

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to ='post/photos')

    like = models.ManyToManyField(User,related_name='likes')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    @property
    def total_likes(self):
        """
            Likes for the post
            :return Integer: likes for the post
        """
        return self.like.count()

    @property
    def number_of_comments(self):
        """
            Comments for the post
            :return Integer: comments for the post
        """
        return Comment.objects.filter(post=self).count()
        

    def  __str__(self):
        """return title and username"""
        return '{} by @{}'.format(self.title,self.user.username)


class Comment(models.Model):
    """comment model."""
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'post: {} {} comment: {}'.format(self.post.title,self.post.user.username,self.comment)

    