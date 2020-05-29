from django.contrib import admin
from first_app.models import user_signup,Friend,Post,Comment
#admin.site.register(users_acc)
admin.site.register(user_signup)
admin.site.register(Friend)
admin.site.register(Post)
admin.site.register(Comment)
