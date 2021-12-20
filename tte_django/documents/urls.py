from django.contrib import admin
from django.urls import path
from .views import DigCertList, DigcertView, DocumentsList,DocumentsDetailView,createCert,selfsign,signValidation,SelfSignList,SelfSignDocumentsDetailView,getDocHash,ReqSignDocViewset,SignigReqViewset,PostReqSignDocViewset,PostSignigReqViewset,getSentReq,getReceive,hashListViewset,signDoc,docValidation
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include

router = DefaultRouter()
router.register("reqsign", ReqSignDocViewset, basename="reqsign")
router.register("signreq", SignigReqViewset, basename="signreq")
router.register("postreqsign", PostReqSignDocViewset, basename="postreqsign")
router.register("postsignreq", PostSignigReqViewset, basename="postsignreq")
router.register("getsentreq", getSentReq, basename="getsentreq")
router.register("getreceive", getReceive, basename="getreceive")
router.register("hashlist", hashListViewset, basename="hashlist")

urlpatterns = [
    path('', DocumentsList.as_view()),
    path('<int:id>', DocumentsDetailView.as_view()),
    path('digcert', DigCertList.as_view()),
    path('digcert<int:id>', DigcertView.as_view()),
    path('selfsigndoc', SelfSignList.as_view()),
    path('selfsigndoc<int:id>', SelfSignDocumentsDetailView.as_view()),
    path('createcert', createCert.as_view()),
    path('selfsign', selfsign.as_view()),
    path('signvalidation', signValidation.as_view()),
    path('getdochash', getDocHash.as_view()),
    path('signdoc', signDoc.as_view()),
    path('docvalidation', docValidation.as_view()),
    # path('reqsign', ReqSignDocViewset.as_view()),
    url('', include(router.urls))
]