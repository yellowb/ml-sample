import struct

# without struct
n = 1
b1 = (n & 0xff000000) >> 24
b2 = (n & 0x00ff0000) >> 16
b3 = (n & 0x0000ff00) >> 8
b4 = (n & 0x000000ff) >> 0
bs = bytes([b1, b2, b3, b4])
print(bs)

# with struct
bs = struct.pack('>I', n)  # set to big-endian, default is little-endian
print(bs)

# unpack
n = struct.unpack('>I', bs)
print(n)
