import sys
import datetime

from cryptography import x509

def load_certificate(file_path):
    with open(file_path, 'rb') as cert_file:
        cert_data = cert_file.read()
        certificate = x509.load_pem_x509_certificate(cert_data)
        return certificate
    
def is_certificate_valid(certificate):
    current_time = datetime.datetime.now()
    not_valid_before = certificate.not_valid_before
    not_valid_after = certificate.not_valid_after

    return not_valid_before <= current_time <= not_valid_after



if __name__ == "__main__":
    certificate_dict = {}

    certificate_path = sys.argv[1]

    # Load the certificate
    certificate = load_certificate(certificate_path)

    # Check if the certificate is valid
    if is_certificate_valid(certificate):
        # Store the certificate in the dictionary with the subject as the key
        certificate_dict[certificate.subject] = certificate
        print(f"Certificate with subject {certificate.subject} is valid.")
    else:
        print("Certificate is not valid.")
