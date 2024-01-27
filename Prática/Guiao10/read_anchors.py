import os
from Ex2 import is_certificate_valid, load_certificate

def trusted_certs(cert):
    trust_certs[cert.subject] = cert
    print(f"Certificate with subject {cert.issuer} is valid.")

if __name__ == "__main__":
    trust_certs = {}
    certs_path = os.scandir("/etc/ssl/certs")
    for certPath in certs_path:
        cert= load_certificate(certPath)
        if is_certificate_valid(cert):
            trusted_certs(cert)
