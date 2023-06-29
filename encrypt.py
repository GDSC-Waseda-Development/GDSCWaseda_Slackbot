from cryptography.fernet import Fernet

json_test = "[\"Test_Key\": \"Test Value\"]"
print(json_test)

key = Fernet.generate_key()
f = Fernet(key)
print(key)
token = f.encrypt(str.encode(json_test))

print(token)

print(f.decrypt(token))

## TODO: (06/15)
## add JSON of Google into parameter (to avoid it getting saved into files)
## save the private key of that encryption into secret
## decrypt it everytime before being used by the Google Docs API