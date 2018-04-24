import zlib

s = 'aa562a2d4e2d52b2524a4cc9cdcc53aa050000'
b = bytearray.fromhex(s)
z = zlib.decompress(b)
print(z)