import os
from django.shortcuts import render
from pyhanko import sign
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import DocumentsSerializer,DigCertSerializer,SelfSignedDocSerializer,SignigReqSeializer,ReqSignDocSerializer,PostReqSignDocSerializer,PostSignigReqSeializer,SignigReqDetailSeializer,HashListSerializer
from .models import Documents,DigitalCert,SelfSignedDocuments,ReqSignDoc,SignigReq,HashList
from rest_framework import permissions,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import requests,json
from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.pdf_utils.reader import PdfFileReader
from pyhanko.sign import fields, signers, timestamps
from pyhanko.sign.general import load_cert_from_pemder
from pyhanko_certvalidator.context import ValidationContext
from pathlib import Path
import hashlib
from pyhanko.sign.validation import validate_pdf_signature


class DocumentsList(ListCreateAPIView):
    # authentication_classes=[]
    serializer_class = DocumentsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        return Documents.objects.filter(author=self.request.user)


class DocumentsDetailView(RetrieveUpdateDestroyAPIView):
    # authentication_classes=[]
    serializer_class = DocumentsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    lookup_field = "id"

    def get_queryset(self):
        # id = self.request.query_params.get('id')
        return Documents.objects.filter(author=self.request.user)



class DigCertList(ListCreateAPIView):
    # authentication_classes=[]
    serializer_class = DigCertSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        return DigitalCert.objects.filter(author=self.request.user)


class DigcertView(RetrieveUpdateDestroyAPIView):
    # authentication_classes=[]
    serializer_class = DigCertSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    lookup_field = "id"

    def get_queryset(self):
        # id = self.request.query_params.get('id')
        return DigitalCert.objects.filter(author=self.request.user)

class SelfSignList(ListCreateAPIView):
    # authentication_classes=[]
    serializer_class = SelfSignedDocSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        return SelfSignedDocuments.objects.filter(author=self.request.user)
       
class SelfSignDocumentsDetailView(RetrieveUpdateDestroyAPIView):
    # authentication_classes=[]
    serializer_class = SelfSignedDocSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    lookup_field = "id"

    def get_queryset(self):
        # id = self.request.query_params.get('id')
        return SelfSignedDocuments.objects.filter(author=self.request.user)

class createCert(APIView):
    def post(self, request):
        
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password = request.data['password']
        email = request.data['email']
        organization = request.data['organization']
        namalengkap =  first_name+' ' +last_name
        os.system('py createCert.py '+'"'+namalengkap+'"'+' '+password+' '+'"'+organization+'"'+' '+email)
        
        f = open(namalengkap+".key", "r")
        
        files = {
        namalengkap+'.key': f,
        }
        response =  requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files, auth=('20dxCr0ToSu5lgXBJbEqJNHMS2i','712c4dd9c8ea398c359e9877f781dcfb'))

        text = json.loads(response.text)
        key_url = text["Hash"]
        f.close()
        f = open(namalengkap+".pem", "r")
        
        files = {
        namalengkap+'.pem': f,
        }
        response =  requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files, auth=('20dxCr0ToSu5lgXBJbEqJNHMS2i','712c4dd9c8ea398c359e9877f781dcfb'))

        text = json.loads(response.text)
        pem_url = text["Hash"]
        f.close()
        
        os.remove(namalengkap+'.key')
        os.remove(namalengkap+'.pem')
        os.remove(namalengkap+'.csr')
        
        
        return Response({'key':key_url,'pem':pem_url})

class selfsign(APIView):
    # parser_classes = (MultiPartParser,)
    def post(self, request):
        password = request.data['password']
        file_url = request.data['file_url']
        key_url = request.data['key_url']
        pem_url = request.data['pem_url']
                
       
        filename = Path('file.pdf')
        link = file_url
        response = requests.get(link)
        filename.write_bytes(response.content)

        link = key_url
        f = requests.get(link)

        file = open('key.key', 'w')
        file.write(f.text)
        file.close()
        
        link = pem_url
        f = requests.get(link)

        file = open('pem.pem', 'w')
        file.write(f.text)
        file.close()

        root_cert = load_cert_from_pemder('signerbcCA.pem')
        vc = ValidationContext(extra_trust_roots=[root_cert])
        tst_client = timestamps.HTTPTimeStamper('http://timestamp.digicert.com')

        signer = signers.SimpleSigner.load(
            'key.key', 'pem.pem',
            ca_chain_files=('signerbcCA.pem',),
            key_passphrase=password.encode()
        )

        with open('file.pdf', 'rb') as inf:
            w = IncrementalPdfFileWriter(inf)
            fields.append_signature_field(
                w, sig_field_spec=fields.SigFieldSpec(
                    'Signature', 
                )
            )

            meta = signers.PdfSignatureMetadata(field_name='Signature',validation_context=vc)

            pdf_signer = signers.PdfSigner(
                meta, signer=signer, timestamper=tst_client
            )
            with open('selfSigned.pdf', 'wb') as outf:
                pdf_signer.sign_pdf(w, output=outf)
        
        f = open("selfSigned.pdf", "rb+")
        
        files = {
        "selfSigned.pdf": f,
        }
        response =  requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files, auth=('20dxCr0ToSu5lgXBJbEqJNHMS2i','712c4dd9c8ea398c359e9877f781dcfb'))

        text = json.loads(response.text)
        signed_url = text["Hash"]
        f.close()
        
        h = hashlib.sha256()
        with open("selfSigned.pdf",'rb') as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                h.update(chunk)
        signed_hash = h.hexdigest()


        os.remove('file.pdf')
        os.remove('key.key')
        os.remove('pem.pem')
        os.remove('selfSigned.pdf')
        return Response({'url':signed_url,'hash':signed_hash})

class signDoc(APIView):
    # parser_classes = (MultiPartParser,)
    def post(self, request):
        password = request.data['password']
        file_url = request.data['file_url']
        key_url = request.data['key_url']
        pem_url = request.data['pem_url']
        id = request.data['id']
                
       
        filename = Path('file.pdf')
        link = file_url
        response = requests.get(link)
        filename.write_bytes(response.content)

        link = key_url
        f = requests.get(link)

        file = open('key.key', 'w')
        file.write(f.text)
        file.close()
        
        link = pem_url
        f = requests.get(link)

        file = open('pem.pem', 'w')
        file.write(f.text)
        file.close()

        root_cert = load_cert_from_pemder('signerbcCA.pem')
        vc = ValidationContext(extra_trust_roots=[root_cert])
        tst_client = timestamps.HTTPTimeStamper('http://timestamp.digicert.com')

        signer = signers.SimpleSigner.load(
            'key.key', 'pem.pem',
            ca_chain_files=('signerbcCA.pem',),
            key_passphrase=password.encode()
        )

        with open('file.pdf', 'rb') as inf:
            w = IncrementalPdfFileWriter(inf)
            fields.append_signature_field(
                w, sig_field_spec=fields.SigFieldSpec(
                    sig_field_name="Signature"+str(id)
                )
            )

            meta = signers.PdfSignatureMetadata(field_name="Signature"+str(id),validation_context=vc)

            pdf_signer = signers.PdfSigner(
                meta, signer=signer, timestamper=tst_client
            )
            with open('selfSigned.pdf', 'wb') as outf:
                pdf_signer.sign_pdf(w, output=outf)
        
        f = open("selfSigned.pdf", "rb+")
        
        files = {
        "selfSigned.pdf": f,
        }
        response =  requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files, auth=('20dxCr0ToSu5lgXBJbEqJNHMS2i','712c4dd9c8ea398c359e9877f781dcfb'))

        text = json.loads(response.text)
        signed_url = text["Hash"]
        f.close()
        
        h = hashlib.sha256()
        with open("selfSigned.pdf",'rb') as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                h.update(chunk)
        signed_hash = h.hexdigest()


        os.remove('file.pdf')
        os.remove('key.key')
        os.remove('pem.pem')
        os.remove('selfSigned.pdf')
        return Response({'url':signed_url,'hash':signed_hash})

class signValidation(APIView):
    def post(self, request):
        file_url = request.data['file_url']

        filename = Path('file.pdf')
        link = file_url
        response = requests.get(link)
        filename.write_bytes(response.content)

        root_cert = load_cert_from_pemder('signerbcCA.pem')
        vc = ValidationContext(extra_trust_roots=[root_cert])

        with open('file.pdf', 'rb') as doc:
            r = PdfFileReader(doc)
            
            length = len(r.embedded_signatures)
            hasil=[]
            for x in range(length):
                sig = r.embedded_signatures[x]
                status = validate_pdf_signature(sig, vc, )
                hasil.append(status.pretty_print_sections())
                isValid=status.bottom_line
        dict={}

        jumlah_ttd=len(hasil)
        i=len(hasil[0])

        for x in range (jumlah_ttd):
            dict[x]={}
            for y in range (i):
                dict[x]['Penandatangan']=hasil[x][0][1]
            for y in range (i):
                dict[x]['Waktu TTE']=hasil[x][2][1]
            for y in range (i):
                dict[x]['Perubahan']=hasil[x][3][1]
    
        os.remove('file.pdf')
        return Response({"details":dict,"status":isValid})

class getDocHash(APIView):
    def post(self, request):
        file_url = request.data['file_url']

        filename = Path('file.pdf')
        link = file_url
        response = requests.get(link)
        filename.write_bytes(response.content)

        h = hashlib.sha256()
        with open("file.pdf",'rb') as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                h.update(chunk)
        signed_hash = h.hexdigest()
        
        os.remove('file.pdf')
        return Response({'hash':signed_hash})


class ReqSignDocViewset(viewsets.ModelViewSet):
    serializer_class = ReqSignDocSerializer

    def get_queryset(self):
        reqsigns = ReqSignDoc.objects.all()
        return reqsigns

class SignigReqViewset(viewsets.ModelViewSet):
    serializer_class = SignigReqSeializer

    def get_queryset(self):
        signreqs = SignigReq.objects.all()
        return signreqs



class PostReqSignDocViewset(viewsets.ModelViewSet):
    serializer_class = PostReqSignDocSerializer

    def get_queryset(self):
        reqsigns = ReqSignDoc.objects.all()
        return reqsigns

class PostSignigReqViewset(viewsets.ModelViewSet):
    serializer_class = PostSignigReqSeializer

    def get_queryset(self):
        signreqs = SignigReq.objects.all()
        return signreqs

class getSentReq(viewsets.ModelViewSet):
    serializer_class = ReqSignDocSerializer
    # lookup_field = 'author'

    def get_queryset(self):
        signreqs = ReqSignDoc.objects.filter(author=self.request.user)
        return signreqs

class getReceive(viewsets.ModelViewSet):
    serializer_class = SignigReqDetailSeializer
    # lookup_field = 'author'

    def get_queryset(self):
        signreqs = SignigReq.objects.filter(signer=self.request.user)
        return signreqs


class hashListViewset(viewsets.ModelViewSet):
    serializer_class = HashListSerializer

    def get_queryset(self):
        hashlist = HashList.objects.all()
        getHash = self.request.query_params.get('hash')
        if getHash is not None:
            queryset = hashlist.filter(hash=getHash)
        return queryset

class docValidation(APIView):
   def post(self, request):
        file_url = request.data['file_url']

        hasil = hashListViewset.as_view({'post':'get_queryset'})
        return Response(hasil)
        # filename = Path('file.pdf')
        # link = file_url
        # response = requests.get(link)
        # filename.write_bytes(response.content)

        # h = hashlib.sha256()
        # with open("file.pdf",'rb') as file:
        #     chunk = 0
        #     while chunk != b'':
        #         chunk = file.read(1024)
        #         h.update(chunk)
        # signed_hash = h.hexdigest()
        
        # os.remove('file.pdf')
        # return Response({'hash':signed_hash})