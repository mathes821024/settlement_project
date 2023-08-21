from django.shortcuts import render

# Create your views here.
from .models import TaskExecution
from django.http import JsonResponse

def create_task(request):
    merchant_id = request.POST.get("merchant_id")
    execution_date = request.POST.get("execution_date")

    existing_task = query_task(merchant_id, execution_date)
    if existing_task:
        return JsonResponse({"status": 3, "message": "正在执行中"})

    new_task = insert_task(merchant_id, execution_date)
    # 进行后续处理
    # ...

    return JsonResponse({"status": 3, "message": "任务已创建"})

def get_task_status(request, merchant_id, execution_date):
    # TODO: Implement logic to get task status based on merchant_id and execution_date
    pass


def query_task(merchant_id, execution_date):
    try:
        task = TaskExecution.objects.get(MERCHANT_ID=merchant_id, EXECUTION_DATE=execution_date)
        return task
    except TaskExecution.DoesNotExist:
        return None

def insert_task(merchant_id, execution_date):
    task = TaskExecution(MERCHANT_ID=merchant_id, EXECUTION_DATE=execution_date)
    task.save()
    return task

def update_task(task_id, status, failure_desc=None):
    task = TaskExecution.objects.get(TASK_ID=task_id)
    task.STATUS = status
    if failure_desc:
        task.FAILURE_DESC = failure_desc
    task.save()

