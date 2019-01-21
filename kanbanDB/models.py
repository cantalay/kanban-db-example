from django.utils import timezone
from django.db import models


class workOrder(models.Model):
    model_type = models.CharField(max_length=10, default="0")
    customer_name = models.CharField(max_length=40)
    create_date = models.DateTimeField(default=timezone.now,null=True)
    deadline = models.DateTimeField(null=True)

class workOrder1(models.Model):
    model_type = models.CharField(max_length=10, default="0")
    customer_name = models.CharField(max_length=40)
    create_date = models.DateTimeField(default=timezone.now,null=True)
    deadline = models.DateTimeField(null=True)

class workOrder2(models.Model):
    model_type = models.CharField(max_length=10, default="0")
    customer_name = models.CharField(max_length=40)
    create_date = models.DateTimeField(default=timezone.now,null=True)
    deadline = models.DateTimeField(null=True)

class workOrder3(models.Model):
    model_type = models.CharField(max_length=10, default="0")
    customer_name = models.CharField(max_length=40)
    create_date = models.DateTimeField(default=timezone.now,null=True)
    deadline = models.DateTimeField(null=True)

class finishedWork(models.Model):
    model_type = models.CharField(max_length=40)
    elapsed_time = models.CharField(max_length=10, default="0")
    work_station = models.CharField(max_length=40)
    worker_id = models.CharField(max_length=10, default="0")

    #create_date = models.DateTimeField(default=timezone.now)

class inventoryControl(models.Model):
    model_number = models.CharField(max_length=10, default="0")
    inventory_amount = models.IntegerField(default=0)
    station = models.CharField(max_length=10,default="null")

class workerInformation(models.Model):
    worker_name = models.CharField(max_length=1, default="")
    working_time = models.CharField(max_length=10, default="0")

class partsInformation(models.Model):
    model_type = models.CharField(max_length=10, default="0")
    felt_type = models.CharField(max_length=10, default="0")
    washer_type = models.CharField(max_length=10, default="0")
    nut_type = models.CharField(max_length=10, default="0")
    spindle_type = models.CharField(max_length=10, default="0")
    body_type = models.CharField(max_length=10, default="0")

class stationInformation(models.Model):
    station_state = models.BooleanField(default=False)
    current_worker = models.CharField(max_length=20, default=0)
