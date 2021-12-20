from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Documents,DigitalCert,SelfSignedDocuments,ReqSignDoc,SignigReq,HashList
from account.serializers import UserSerializer
from rest_framework import serializers



class DigCertSerializer(ModelSerializer):

    class Meta:
        model = DigitalCert
        
        fields = [
            'author','status','key_url','cert_url','id'
        ]

class SelfSignedDocSerializer(ModelSerializer):

    class Meta:
        model = SelfSignedDocuments

        fields=[
            'file_name','size','status','time','file_url','signed_url','id','ori_id'
        ]

class DocumentsSerializer(ModelSerializer):
    class Meta:
        model = Documents
        
        fields = [
            'file_name','size','status','time','file_url','id'
        ]

class SignigReqSeializer(ModelSerializer):
    signer = UserSerializer(read_only=True)

    class Meta:
        model = SignigReq
        # signer = serializers.CharField(source="Documents.file_name", read_only=True)
        fields = [
                'id','signer','doc_url','status'
            ]

class ReqSignDocSerializer(ModelSerializer):
    signer = SignigReqSeializer(many=True,read_only=True)
    original_file = DocumentsSerializer(read_only=True)
    author = UserSerializer(read_only=True)
    class Meta:
        model = ReqSignDoc

        fields = [
                'id','author','original_file','signer','signed_url','status'
            ]


class PostSignigReqSeializer(ModelSerializer):
    

    class Meta:
        model = SignigReq
        # signer = serializers.CharField(source="Documents.file_name", read_only=True)
        fields = [
                'id','signer','doc_url','status'
            ]

class PostReqSignDocSerializer(ModelSerializer):
    
    class Meta:
        model = ReqSignDoc

        fields = [
                'id','author','original_file','signer','signed_url'
            ]


class SignigReqDetailSeializer(ModelSerializer):
    signer = UserSerializer(read_only=True)
    doc_url = ReqSignDocSerializer(read_only=True)
    class Meta:
        model = SignigReq
        # signer = serializers.CharField(source="Documents.file_name", read_only=True)
        fields = [
                'id','signer','doc_url','status'
            ]

class HashListSerializer(ModelSerializer):
    
    class Meta:
        model = HashList

        fields = [
                'doc_id','hash'
            ]