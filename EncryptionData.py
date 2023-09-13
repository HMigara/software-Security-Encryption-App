from cryptography.fernet import Fernet
import rsa
import base64


def Encryption(message):
    
    #open massege key
    skey=open('message.key','rb')
    key=skey.read()

    #create cyper
    cipher=Fernet(key)

    #encypte data
    encrypted_data=cipher.encrypt(bytes(message,'utf-8'))
    edata=open('EncryptedFile','wb')
    edata.write(encrypted_data)
    

    public_key = open('public_key.key','rb')
    pubkey = public_key.read()


    #encrypt the data
    pubkey = rsa.PublicKey.load_pkcs1(pubkey)
    encrypted_key = rsa.encrypt(key,pubkey)

    #write encrypted_data
    edata = open ("EncryptedKey","wb")
    edata.write(encrypted_key)
    
    #create kye function need to ron here


#Encryption("Hello")