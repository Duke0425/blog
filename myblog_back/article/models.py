from django.db import models

# Create your models here.
# 文章分类表
class Category(models.Model):
    """
    文章分类
    """
    name = models.CharField(max_length=20,unique=True)
    nickname = models.CharField(max_length=20,default=None)
    high_category = models.ForeignKey('self',
                                 on_delete=models.CASCADE,
                                      related_name='hcate',)
    class Meta:
        db_table = 'category'

# 文章内容表
class Blog(models.Model):
    """
    博客文章表
    """
    title = models.CharField(max_length=100, unique=True)
    content = models.CharField(default='', max_length=9999)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    # 存图片的地址,数据库中icon字段的类型是varchar
    title_pic = models.ImageField(upload_to='upload',null=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='cate')

    class Meta:
        db_table = 'Blog'
