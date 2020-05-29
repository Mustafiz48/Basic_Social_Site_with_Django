from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

gender=(
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others')
)

class user_signup(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Gender=models.CharField(max_length=264,choices=gender,default='Male')
    Mobile=models.CharField(max_length=11)
    Birth=models.DateField()
    propic=models.ImageField(blank='True')
    friends = models.ManyToManyField('user_signup', blank=True)


    def __str__(self):
         return self.user.username


class FriendRequest(models.Model):
	to_user = models.ForeignKey(User, related_name='%(class)s_to_user',on_delete=models.CASCADE)
	from_user = models.ForeignKey(User,related_name='%(class)s_from_user',on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True) # set when created

	def __str__(self):
		return "From {}, to {}".format(self.from_user.username, self.to_user.username)



class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True,on_delete=models.CASCADE)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)




class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)





class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
