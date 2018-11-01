from django.db import models

# Create your models here.
import uuid


def unique_uuid():
    return uuid.uuid1().hex


class Repair(models.Model):
    number_id = models.CharField(primary_key=True, max_length=32, default=unique_uuid)
    title = models.CharField(max_length=20, db_index=True)
    problem_desciption = models.CharField(max_length=255, db_index=True)
    status = models.CharField(max_length=1, db_index=True, default=0)
    finish_status = models.CharField(max_length=1, db_index=True, default=0)
    weibao_account = models.CharField(max_length=20, db_index=True, null=True)
    receive_time = models.DateTimeField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    reason = models.CharField(max_length=255, db_index=True, null=True)
    solve_way = models.CharField(max_length=255, db_index=True, null=True)
    remark = models.CharField(max_length=255, db_index=True, null=True)
    customer_id = models.CharField(max_length=32, db_index=True)
    depot_id = models.CharField(max_length=32, db_index=True)

    def detail_info(self):
        return {
            'number_id': self.number_id,
            'title': self.title,
            'problem_desciption': self.problem_desciption,
            'status': self.status,
            'finish_status': self.finish_status,
            'weibao_account': self.weibao_account,
            'receive_time': self.receive_time,
            'create_time': self.create_time,
            'update_time': self.update_time,
            'reason': self.reason,
            'solve_way': self.solve_way,
            'remark': self.remark,
            'customer_id': self.customer_id,
            'depot_id': self.depot_id
        }

    class Meta:
        db_table = 'repair_table'



