import hashlib
str="hello"
output=hashlib.md5(str.encode())
print("the deired hash is:")
print(output.hexdigest())

import hashlib
str="hello world"
output=hashlib.md5(str.encode())
print("the deired hash is:")
print(output.hexdigest())