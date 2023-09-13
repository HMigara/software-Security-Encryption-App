import hashlib


def hash_pw(password):
    # Encode the password as bytes
    password_bytes = password.encode('utf-8')
    
    # Use SHA-256 hash function to create a hash object
    hash_object = hashlib.sha256(password_bytes)
    
    # Get the hexadecimal representation of the hash
    password_hash = hash_object.hexdigest()
    
    return password_hash
