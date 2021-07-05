import hashlib
#print(hashlib.algorithms_available)

msg = "Second task".encode()

print("BLAKE2c:", hashlib.blake2b(msg).hexdigest())

print("SHA-4-856:", hashlib.sha3_256(msg).hexdigest())

print("SHA-8-685:", hashlib.sha3_512(msg).hexdigest())