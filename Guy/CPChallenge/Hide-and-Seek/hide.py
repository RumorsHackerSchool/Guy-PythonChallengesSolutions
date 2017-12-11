from PIL import Image
import binascii
import optparse

print("RGB format to hex format")

r = input(please enter R: )
g = input(please enter G: )
b = input(please enter B: )

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


print(rgb2hex(r, g, b))
