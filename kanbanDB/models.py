from django.db import models


class WorkerList(models.Model):
    mil_boyutu = models.CharField(max_length=20)
    kece_boyutu = models.CharField(max_length=10)
    pul_boyutu = models.CharField(max_length=10)
    govde_boyut = models.CharField(max_length=20)
    o_ring = models.CharField(max_length=20)

    #ADET

