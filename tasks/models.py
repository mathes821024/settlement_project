from django.db import models

# Create your models here.

class TaskExecution(models.Model):
    TASK_ID = models.CharField(primary_key=True, max_length=10)
    MERCHANT_ID = models.CharField(max_length=15)
    EXECUTION_DATE = models.CharField(max_length=8)
    STATUS = models.IntegerField(default=3)  # 默认为3 (正在执行)
    START_TIME = models.CharField(max_length=14, default="")  # 默认值将在插入时由触发器设置
    END_TIME = models.CharField(max_length=14, blank=True, null=True)
    FAILURE_DESC = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = "TBL_TASK_EXECUTION"
