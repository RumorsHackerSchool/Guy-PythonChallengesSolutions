#!/usr/bin/env python3
import zlib

websocket_payload_packet_1 = bytes.fromhex("""
aa562a2d4e2d52b2524a4cc9cdcc53aa0500
""".replace("\n", ""))



# Data from frame 1
data = websocket_payload_packet_1
# Needed per spec (https://tools.ietf.org/html/rfc7692#section-7.2.2)
data += b'\0\0\xff\xff'


z = zlib.decompressobj(wbits=-15)
out = z.decompress(data)
print(out)