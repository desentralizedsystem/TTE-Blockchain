import sys
import os

caPass='rESTonThRONG'
nama = sys.argv[1]
password = sys.argv[2]
organization = sys.argv[3]
email = sys.argv[4]
keyFile = nama+'.key'
reqFile = nama+'.csr'
pemFile = nama+'.pem'

# print('openssl genrsa -des3 -passout pass:'+password+ ' -out '+'"'+keyFile+'"'+' 2045')
os.system('openssl genrsa -des3 -passout pass:'+password+ ' -out '+'"'+keyFile+'"'+' 2045')

# print('openssl req -key '+'"'+keyFile+'"'+' -new -out '+'"'+reqFile+'"'+' -passin pass:'+password+' -subj "/C=ID/O='+organization+'/CN='+nama+'/emailAddress='+email+'"')
os.system('openssl req -key '+'"'+keyFile+'"'+' -new -out '+'"'+reqFile+'"'+' -passin pass:'+password+' -subj "/C=ID/O='+organization+'/CN='+nama+'/emailAddress='+email+'"')

# print('openssl x509 -req -in '+'"'+reqFile+'"'+' -CA signerbcCA.pem -CAkey signerbcCA.key -passin pass:'+caPass+' -CAcreateserial -out '+'"'+pemFile+'"'+' -days 2000 -sha256 -extfile certEx.ext')
os.system('openssl x509 -req -in '+'"'+reqFile+'"'+' -CA signerbcCA.pem -CAkey signerbcCA.key -passin pass:'+caPass+' -CAcreateserial -out '+'"'+pemFile+'"'+' -days 2000 -sha256 -extfile certEx.ext')


