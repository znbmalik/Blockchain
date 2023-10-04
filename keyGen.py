from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# create public and private key
def generate_key():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key
'''print( generate_key())
# Generate keys
#private_key, public_key = generate_key()

# Print the keys
print("Public Key:")
print(public_key)

print("\nPrivate Key:")
print(private_key)'''

def sign(message, private_key):
    message = bytes(str(message), 'utf-8')
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verify(message, signature, public_key):
    message = bytes(str(message), 'utf-8')
    #public_key = private_key.public_key()
    try:
        public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
        )
        return True
    except:
        return False


if __name__ == '__main__':
    pr , pu = generate_key()
    print (pr)
    print (pu)
    message = "Hello World"
    signature = sign(message,pr)
    print (signature)
    print (verify(message,signature,pu))