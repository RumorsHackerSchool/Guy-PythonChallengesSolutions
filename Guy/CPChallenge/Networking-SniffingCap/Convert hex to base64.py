##Hex to bin and bin to base64
import binascii
import base64
import zlib
base64string = str(input("Enter base64 string ONLY: "))
#var1 = binascii.a2b_hex(HexDecimal)
#print (var1)
string = base64.b64decode(base64string)
hexstring = binascii.hexlify(string)

print (string)
print (hexstring)

z = zlib.decompressobj(wbits=-15)
out = z.decompress(hexstring)
print(out)