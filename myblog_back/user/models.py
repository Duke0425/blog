from django.db import models

# Create your models here.
# 用户表
class User(models.Model):
    username = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=150,null=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'

# cookie表
class UserToken(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    token = models.CharField(max_length=20)

    class Meta:
        db_table = 'user_token'