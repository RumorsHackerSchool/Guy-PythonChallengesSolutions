import argparse
import math
import random
from PIL import Image


def do2(i, p, s, w1, w2, x):
    bc = 0

    s = list(s)
    print("this is the 's' - ",s)
    while len(s) > 0:
        letter = s.pop(0)
        print(letter)
        for loop in range(8):
            ##the "<<" sing is bitwise and move the bits to left
            ##the ord() return an integer representing the Unicode code point of the character
            ##in my case ord("A") equal to 65
            ##(number) & 0xFF) take the numbers and use & which give you the original number anyway
            ##int((math.sqrt(math.sqrt(math.sqrt(16777217 - 1))) - calculate the squr root of 16777217
            ##which is 4096.0 and then calculate it again - 64.0 - 1 = 63
            s2 = ((ord(letter) << loop) & 0xFF) >> int(63)
            x2 = ((x * (2 ** loop)) & 0xFF) >> int(7)
            pc = int(bc / 3)
            q = ((w1 + pc) % i[0])
            v = (w2 + int((pc + w1) / i[0]))
            pt = list(p[q, v])
            pt[bc % 3] = (pt[bc % 3] | (s2 ^ x2))
            if pt[bc % 3] % 2 and not s2 ^ x2:
                pt[bc % 3] -= 1

            p[q, v] = tuple(pt)
            bc += 1
        x += 1
        x &= 0xff


def mb(*args):
    return [(args[int(i / 2)] >> ((i % 2) * 8)) & 0xff for i in range(len(args) * 2)]


def do(i, s):
    print("in do print ths S - ",s)
    p = i.load()##load the image
    ##random.randint - chose number between 0 and width
    n1 = random.randint(0, (i.size[0] - int(len(s) / i.size[0]) - 1) % 0xFFFF)

    ##random.randint - chose number between 0 and height
    n2 = random.randint(0, (i.size[1] - int(i.size[0] % len(s)) - 1) % 0xFFFF)

    ##i.size - give us two number with width and height
    ##the p is the image object - <PixelAccess object at 0x7f413b896690>
    do2(i.size, p, "".join([chr(j) for j in mb(n1, n2, len(s) & 0xFFFF)]), 0, 0, 0)
    x = 97
    do2(i.size, p, s, n1, n2, x)


def parse_args():
    #this function take the arguments for makeing commands for the user
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=str, help='image file')#image file
    parser.add_argument("string", type=str)#the string to hide
    parser.add_argument("out", type=str, help='png file')#the new output image
    return parser.parse_args()


def main():
    args = parse_args()#the arguments for the image
    image = Image.open(args.image)#opening the image using the agruments
    print("in main print image - ",image)
    print("in main print args.string - ", args.string)
    do(image, args.string)
    image.save(args.out if args.out.endswith("png") else ".".join([args.out, "png"]))


if __name__ == "__main__":
    main()
