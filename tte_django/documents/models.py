from typing import Sized
from django.db import models
# from django.contrib.auth.models

from account.models import Account 



# Create your models here.

class Documents (models.Model):
    file_name   = models.CharField(max_length=225, unique=False)
    author      = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    size        = models.IntegerField ()
    status      = models.CharField (max_length=225, unique=False)
    time        = models.DateTimeField(auto_now_add=True)
    file_url    = models.URLField()


class DigitalCert (models.Model):
    author      = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    status      = models.CharField (max_length=225, unique=False)
    key_url    = models.URLField()
    cert_url    = models.URLField()

class SelfSignedDocuments (models.Model):
    file_name   = models.CharField(max_length=225, unique=False)
    author      = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    size        = models.IntegerField ()
    status      = models.CharField (max_length=225, unique=False)
    time        = models.DateTimeField(auto_now_add=True)
    file_url    = models.URLField()
    signed_url    = models.URLField()
    ori_id        = models.BigIntegerField(blank=True)

class ReqSignDoc (models.Model):
    author      = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    original_file = models.ForeignKey(to=Documents, on_delete=models.CASCADE)
    status      = models.CharField (max_length=225, unique=False,default="Pending")
    signed_url    = models.URLField(blank=True)


class SignigReq (models.Model):
    signer      = models.ForeignKey(to=Account,on_delete=models.CASCADE)
    doc_url     = models.ForeignKey(to=ReqSignDoc,on_delete=models.CASCADE,related_name='signer')
    status      = models.CharField (max_length=225, unique=False,default="Pending")


class HashList (models.Model):
    doc_id      = models.ForeignKey(to=Documents,on_delete=models.CASCADE)
    hash      = models.CharField(max_length=225)