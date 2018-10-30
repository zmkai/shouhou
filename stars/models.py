from django.db import models

# Create your models here.

def unique_uuid():
    return uuid.uuid1().hex()

import uuid

class Stars(models.Model):
    star_id = models.CharField(primary_key=True,default=unique_uuid)
    weibao_id = models.CharField(max_length=20, db_index=True)
    create_time = models.DatetimeField(auto_now_add=True)
    update_time = models.DatetimeField(auto_now=True, null=True)
    star=models.FloatField(default=5)

    class Meta:
        db_table = 'star_table'


