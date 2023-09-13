import rsa
from cryptography.fernet import Fernet

def Decryption():
    private_key = open('private_key.key','rb')
    prikey = private_key.read()
    prkey = rsa.PrivateKey.load_pkcs1(prikey)

    #read the encrypted file
    encrypted_data = open("encryptedKey","rb")
    ekey= encrypted_data.read()
    
    #decripte the data
    dkey=rsa.decrypt(ekey,prkey)

    cipher=Fernet(dkey)

    encrypted_data=open('EncryptedFile','rb')
    edata=encrypted_data.read()

    decripted_data=cipher.decrypt(edata)
    msg =decripted_data.decode()

    print(msg)
    return msg

#Decryption()