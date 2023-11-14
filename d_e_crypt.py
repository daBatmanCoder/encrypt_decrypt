from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import random
import string

# This will simulate the client's behaviour - sending the identity and fetching the public key from the a database later.
def get_public_key(identity):
	return """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyyyva1KASj+AyJDCHLvN
I3k6r8rOfOA4oVfUEWjxbNL7BI/CJVJhBnMDtKQsiLWnPoTUpAuOPPWXR25M4i/I
p4pmnWEZqq4h07yZLLtUX3dZy3EtXLD2xj8Yk19HphqX3G9xJMMv2bnLGYh2lj53
s7K8TrnpyzqG/ugJ1qHOd0DnnAoUg1zx0+vkv9ky3wVldIZTCmYtUmPZVIOrXoZJ
iXRq0kpkUnFcswT29lUABfxou+yD+wqXm205NVtO5exjo4c4CWEWukR/W+OKhrTF
8nMu0wWUyr3XvBPIHZVOpA3+CEXdIGpHzELWJ83cyCHGRPO6s4QhnvxF/Cttgwcm
yQIDAQAB
-----END PUBLIC KEY-----"""

# Random generator 
def generate_username_password():
    # Define the character set for the username and password
    char_set = string.ascii_letters + string.digits  # A-Z, a-z, 0-9

    # Define the length of the username and password
    username_length = random.randint(10, 16)  # Random length between 8 and 12
    password_length = random.randint(12, 16)  # Random length between 8 and 16

    # Generate the username and password
    username = ''.join(random.choice(char_set) for _ in range(username_length))
    password = ''.join(random.choice(char_set) for _ in range(password_length))

    return username + " " + password

# Matthies data
data_to_encrypt_matthias = "alice q1w2e3"

#  The username and password are separated by a space -
#  In the example run of this function, it generated: 'ZNOlvDRP tuqP1U6rnS'
data_to_encrypt_random = generate_username_password()

# This will output the public key of the user from the identity - NFT
public_key_of_identity = get_public_key("") 

# Serialize the public key.
public_key = serialization.load_pem_public_key(public_key_of_identity.encode(), backend=default_backend())

# Encryption the data (matthies data)
encrypted_data_matthias = public_key.encrypt(
		data_to_encrypt_matthias.encode(),
		padding.OAEP(
			mgf=padding.MGF1(algorithm=hashes.SHA256()),
			algorithm=hashes.SHA256(),
			label=None
		)
	)

# Encryption the data (random data)
encrypted_data_random= public_key.encrypt(
		data_to_encrypt_random.encode(),
		padding.OAEP(
			mgf=padding.MGF1(algorithm=hashes.SHA256()),
			algorithm=hashes.SHA256(),
			label=None
		)
	)

# Preparing the json of the data to be sent back to the client to decrypt
json_of_data_matthias = {
      "data": data_to_encrypt_matthias,
      "encrypted_data": encrypted_data_matthias
}

json_of_data_random = {
      "data": data_to_encrypt_random,
      "encrypted_data": encrypted_data_random
}
           
                                                                                                                                                         
####################################################################################################################################################################################
####################################################################################################################################################################################
####################################################################################################################################################################################                                                                                                                                                       
########## ######   #######  #######  #######  #     #  #######  #######     #     #######  #     #           #######  #######  #######     #     #######  ####### #################
########## #     #  #        #        #     #  #     #  #     #     #        #     #     #  ##    #           #        #        #     #     #     #     #     #    #################
########## #     #  ####     #        #######  #######  #######     #        #     #     #  # ### #           #######  #        #######     #     #######     #    #################
########## #     #  #        #        #    #         #  #           #        #     #     #  #    ##                 #  #        #    #      #     #           #    #################
########## ######   #######  #######  #    ##  #######  #           #        #     #######  #     #           #######  #######  #    ##     #     #           #    #################
####################################################################################################################################################################################
####################################################################################################################################################################################
####################################################################################################################################################################################
####################################################################################################################################################################################
                                                                                                                                                     

# Decryption Script - 

# Private to decrypt the data
private_key_pem = """-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDLLK9rUoBKP4DI
kMIcu80jeTqvys584DihV9QRaPFs0vsEj8IlUmEGcwO0pCyItac+hNSkC4489ZdH
bkziL8inimadYRmqriHTvJksu1Rfd1nLcS1csPbGPxiTX0emGpfcb3Ekwy/ZucsZ
iHaWPnezsrxOuenLOob+6AnWoc53QOecChSDXPHT6+S/2TLfBWV0hlMKZi1SY9lU
g6tehkmJdGrSSmRScVyzBPb2VQAF/Gi77IP7CpebbTk1W07l7GOjhzgJYRa6RH9b
44qGtMXycy7TBZTKvde8E8gdlU6kDf4IRd0gakfMQtYnzdzIIcZE87qzhCGe/EX8
K22DBybJAgMBAAECggEAFbF8O2vQKd1U7VVTfIjq0tZPV1TCrl+sfEGp8X/wgyuV
xLtqwdxlYrBmHWQII0KuDEVXhPp84fJhCC31RJNQi98BrN0gxfIYx4hUHIwV6qmO
K2Q2sTZt6uXyxE2Ak3I0c8NsY735fnhRgLTq4Ijj9ApqA8fi+CGUJ2R0JHgbWO0i
5cFvthXp8M91mdgnL/VTeuIUnCjBxjZwwr+CQTNoUFbLoa8mbw9EGIH3VDB1ubjy
7B6M76g68iIzL8xhhuQeLBM0jtcKPKK0eSoULwLeytSxm1jh93GvhjFKQNfDi4/r
/HQHOsk8fZK5WxZwN5/hUp6Z7BqIQKTuBsR18KCm+QKBgQDxahybhX4z+77Pe7pk
38aiZkSZqaupWc8CxfHzLjo2jYSyEImgLHSqCgIQwljrfGNNMN5OLAbOxqsB4hmX
LMDfuDZYlvloR9g7T4tYanSpwLhDCHRAhyqmqokgv7fWF1FjHlZJGy5OAnsOsMH0
odWGfQeiUGmY8aXk3hJ/F92AZQKBgQDXcyCVFnf02/wLd/g09cTwFWN0jbt8yIUS
OCWTW9On37565KmfSCZTSu6ZzxemVpx30zgrqspAaZjrNhP+UkoBlHNUoBhvxXQb
9NZKLf3vm9NhTJbg5q5uE98cbqNztWt+26rY+IEOMOd7cwedg9KSMAIGsOb5Kv+c
7Q5silj8lQKBgQDK0i9+qcTBv7srbfPHVAn53pm7z8Sc3wsAdXU0rZ3Sv0rAnwxB
OZg6U3YwxlcWYMa8z1W1r1940YhSaLa/P6Y7TvS5sP2REusjyUx019tz0qn8B1pD
7Et1Asl6bhfxEl4aPB6aBO/+Mi9YxD/vWxedieWkBJLzH/IUOk6n4FED0QKBgQCD
O1X6WdBBbomMtsuR/q2xi2WkBfzQmhcsLNT+eC1pEMkmdAe5xKnLjFXfjBwcrp7q
AdcyCfrd1zRU+QCepaL8aV8Cie24jy4VJUIttuv5OhI8LvmsDfbrh+EboWygOz45
7DWZqWx6p2Eoeb2GvVfSwblKOBDIbt95x49En9RqLQKBgQDsT+d8ysu7Pr/9mepN
lbDjmXfPAX76JsMhXhOtNuJrKDT08kuLDBuuCf7GvF2HsWSxHL9bCNusbbAMH2W8
ZDYtCIZRDw8kOo+5UILrC3oeyEtc/MR5nRaUfad/WDz7aaMSu8fSFP5+Q1OXDTtq
k0BgHtyaimeiX3UVcVA+H3Y59Q==
-----END PRIVATE KEY-----"""

# Fetching back matthies's data from the server ( simulation )
data_from_the_server_matthias = json_of_data_matthias['data']
encrypted_data_from_server_matthias = json_of_data_matthias['encrypted_data']

# Fetching back the random data from the server ( simulation )
data_from_the_server_random = json_of_data_random['data']
encrypted_data_from_server_random = json_of_data_random['encrypted_data']

# Serializating the private key
private_key = serialization.load_pem_private_key(
    private_key_pem.encode(),
    password=None,  # No password protection for the private key
    backend=default_backend()
)

# Decrypt matthies's data.
decrypted_data_matthias = private_key.decrypt(
    encrypted_data_from_server_matthias,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decrypt the random data
decrypted_data_random = private_key.decrypt(
    encrypted_data_from_server_random,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

######################################################################################################
# Sanity check to see that the data is indeed equal (before and after the encryption and decryption) #
######################################################################################################


print("(Matthias) The original data was: " + data_from_the_server_matthias +  " The decrypted data is: " + decrypted_data_matthias.decode('utf-8'))
if data_from_the_server_matthias == decrypted_data_matthias.decode('utf-8'):
      print("Matthias data is the same!")


print("(Random) The original data was: " + data_from_the_server_random +  " The decrypted data is: " + decrypted_data_random.decode('utf-8'))
if data_from_the_server_random == decrypted_data_random.decode('utf-8'):
      print("The random data is the same!")
      
