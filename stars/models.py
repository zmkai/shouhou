from django.db import models
from util.uuid_util import unique_uuid


class Stars(models.Model):
    star_id = models.CharField(primary_key=True, max_length=32, default=unique_uuid)
    weibao_account = models.CharField(max_length=20, db_index=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    star=models.FloatField(default=5)

    class Meta:
        db_table = 'star_table'


