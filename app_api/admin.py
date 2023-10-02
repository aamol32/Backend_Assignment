from django.contrib import admin
from .models import User_detail,Post_detail,Follower
# Register your models here.
admin.site.register(User_detail)
admin.site.register(Post_detail)
admin.site.register(Follower)