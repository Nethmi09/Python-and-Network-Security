text = 'Hi...hello world'

import hashlib
m = hashlib.md5()
m.update(text.encode('utf-8'))
print(m.hexdigest())



text = 'Hi...My name is Nethmi Udara'

import hashlib
m = hashlib.md5()
m.update(text.encode('utf-8'))
print(m.hexdigest())

#One-Liner Trial
text = 'My age is 23 years old';import hashlib;m=hashlib.md5();m.update(text.encode('utf-8'));print(m.hexdigest())
