import os
from Ex2 import is_certificate_valid, load_certificate
from read_anchors import trusted_certs
import sys

def build_certificate_chain(cert, intermediate_certs, trusted_certs):
    certificate_chain = [cert]
    
    while cert.issuer not in trusted_certs:
        issuer_subject = cert.issuer
        if issuer_subject in intermediate_certs:
            issuer_cert = intermediate_certs[issuer_subject]
            if not is_certificate_valid(issuer_cert):
                print(f"Intermediate certificate {issuer_cert.subject} is not valid.")
                return None
            certificate_chain.append(issuer_cert)
            cert = issuer_cert
        else:
            print("Chain is untrusted. Missing root certificate.")
            return None

    # Add the trusted root certificate to the chain
    certificate_chain.append(trusted_certs[cert.issuer])
    
    return certificate_chain

if __name__ == "__main__":
    trust_certs = {}
    intermediate_certs = {}  # Dictionary to store user-specified intermediate roots

    certs_path = os.scandir("/etc/ssl/certs")
    for cert_path in certs_path:
        cert = load_certificate(cert_path)
        if is_certificate_valid(cert):
            trusted_certs(cert)

    # Assuming user-provided intermediate certificates are stored in a dictionary called 'user_provided_intermediates'
    # Update this dictionary with the actual user-provided intermediate certificates
    user_provided_intermediates = {}

    # Load the user certificate
    user_certificate_path = sys.argv[1]
    user_certificate = load_certificate(user_certificate_path)

    # Build the certificate chain
    certificate_chain = build_certificate_chain(user_certificate, user_provided_intermediates, trusted_certs)

    if certificate_chain:
        print("Certificate chain:")
        for cert in certificate_chain:
            print(f"- {cert.subject}")
