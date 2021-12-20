from django.contrib import admin

from documents.models import Documents,DigitalCert,SelfSignedDocuments,ReqSignDoc,SignigReq,HashList


admin.site.register(Documents)
admin.site.register(DigitalCert)
admin.site.register(SelfSignedDocuments)
admin.site.register(ReqSignDoc)
admin.site.register(SignigReq)
admin.site.register(HashList)
