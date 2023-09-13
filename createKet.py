import rsa
from cryptography.fernet import Fernet

def KeyGeneration():
    # Create symmetric key
    key = Fernet.generate_key()

    # Write the symmetric key to a file
    with open('message.key', 'wb') as k:
        k.write(key)

    # Create private and public key using rsa.newkeys() function
    (pubkey, privkey) = rsa.newkeys(2048)

    # Write the private key to a file
    with open('private_key.key', 'wb') as private_key_file:
        private_key_file.write(privkey.save_pkcs1('PEM'))

    # Write the public key to a file
    with open('public_key.key', 'wb') as public_key_file:
        public_key_file.write(pubkey.save_pkcs1('PEM'))

#KeyGeneration()