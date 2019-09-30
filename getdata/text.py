import hashlib
a= hashlib.md5('Dwzx170322'.encode('utf8')).hexdigest()
b =hashlib.md5('Dwzx170322'.encode('utf8')).hexdigest()
print(a==b)