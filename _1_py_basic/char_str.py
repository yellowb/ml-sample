# char to int
c1 = '中'
print(ord(c1))

# int to char
o1 = 12345
print(chr(o1))

# encode str to bytes
s1 = '我爱中华人民共和国'
print(s1.encode('UTF-8'))

# decode bytes to str
b1 = b'\xe6\x88\x91\xe7\x88\xb1\xe4\xb8\xad\xe5\x8d\x8e\xe4\xba\xba\xe6\xb0\x91\xe5\x85\xb1\xe5\x92\x8c\xe5\x9b\xbd'
print(b1.decode('UTF-8'))
