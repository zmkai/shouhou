from django.db import models

# Create your models here.
import uuid


def unique_uuid():
    return uuid.uuid1().hex()


class Comment(models.Model):
    comment_id=models.CharField(primary_key=True,max_length=32,default=unique_uuid)
    number_id=models.CharField(max_length=32)
    weibao_account=models.CharField(max_length=20)
    create_time=models.DateTimeField(auto_now_add=True,null=True)
    update_time=models.DateTimeField(auto_now=True,null=True)
    remark=models.CharField(max_length=255,null=True)
    comments=models.CharField(max_length=255,null=True)

    class Meta:
        db_table = 'comment_table'

