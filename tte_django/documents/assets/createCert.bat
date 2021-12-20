set caPass=rESTonThRONG

openssl genrsa -des3 -passout pass:%2 -out %1.key 2045
openssl req -key %1.key -new -out %1.csr -passin pass:%2 -subj "/C=ID/O=%3/CN=%1/emailAddress=%4"

openssl x509 -req -in %1.csr -CA signerbcCA.pem -CAkey signerbcCA.key -passin pass:%caPass% -CAcreateserial -out %1.pem -days 2000 -sha256 -extfile certEx.ext