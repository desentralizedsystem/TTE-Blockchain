
from pyhanko import stamp
from pyhanko.pdf_utils import text, images
from pyhanko.pdf_utils.font import opentype
from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign import fields, signers, timestamps
from pyhanko.sign.general import load_cert_from_pemder
from pyhanko_certvalidator.context import ValidationContext

root_cert = load_cert_from_pemder('signerbcCA.pem')
vc = ValidationContext(extra_trust_roots=[root_cert])
tst_client = timestamps.HTTPTimeStamper('http://timestamp.digicert.com')

signer = signers.SimpleSigner.load(
    'ashimos.key', 'ashimos.pem',
    ca_chain_files=('signerbcCA.pem',),
    key_passphrase=b'1234'
)
with open('document-signed.pdf', 'rb') as inf:
    w = IncrementalPdfFileWriter(inf)
    fields.append_signature_field(
        w, sig_field_spec=fields.SigFieldSpec(
            'Signature1', 
        )
    )

    meta = signers.PdfSignatureMetadata(field_name='Signature1',validation_context=vc)

    pdf_signer = signers.PdfSigner(
        meta, signer=signer, timestamper=tst_client
    )
    with open('document-signed2.pdf', 'wb') as outf:
        pdf_signer.sign_pdf(w, output=outf)