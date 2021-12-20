from pyhanko.sign.general import load_cert_from_pemder
from pyhanko_certvalidator import ValidationContext
from pyhanko.pdf_utils.reader import PdfFileReader
from pyhanko.sign.validation import validate_pdf_signature

root_cert = load_cert_from_pemder('signerbcCA.pem')
vc = ValidationContext(extra_trust_roots=[root_cert])

with open('document-signed2.pdf', 'rb') as doc:
    r = PdfFileReader(doc)

    length = len(r.embedded_signatures)-1
    sig = r.embedded_signatures[length]
    status = validate_pdf_signature(sig, vc)
    print(status.pretty_print_details())
    
    
    # length = len(r.embedded_signatures)-1

    # for x in range(length+1):
    #     sig = r.embedded_signatures[x]
    #     status = validate_pdf_signature(sig, vc)
    #     print(status.pretty_print_details())
    #     # print(x)

