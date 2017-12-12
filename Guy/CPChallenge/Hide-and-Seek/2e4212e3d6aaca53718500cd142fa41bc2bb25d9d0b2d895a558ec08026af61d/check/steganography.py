import argparse
import math
import random
from PIL import Image


def do2(i, p, s, w1, w2, x):
    bc = 0
    s = list(s)
    while len(s) > 0:
        c = s.pop(0)
        for b in range(1 + 1 + 1 + 1 + 1 + 2 + 2 - 1):
            s2 = ((ord(c) << b) & 0xFF) >> int((math.sqrt(math.sqrt(math.sqrt(16777217 - 1))) - 1))
            x2 = ((x * (2 ** b)) & 0xFF) >> int((0x1523486567 << 23 >> 54) / 7 + 1)
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


def do(i, s): ##take the image and the message
    p = i.load() ##read the img or more likely called it - look  more like <PixelAccess object at 0x7fa7be4a7b90>
    n1 = random.randint(0, (i.size[0] - int(len(s) / i.size[0]) - 1) % 0xFFFF)
    '''
    i.size is the size of the image in tuple the first i.size[0] is width
    len(s) is the len of the message we want to hide so if it is hello is equal to 5 and we divide it with image width which is 1116
    because of the int its equal to 0 so we subtract a 1 from it and it will be 1115, and the 1115 % 0xFFFF have a remainder of 1115 (it like  1115%65535)
    random.randint generate randome number between 0 and 1115
    p = <PixelAccess object at 0x7fa7be4a7b90>
    n1 = some randome number between 0 and 1115
    '''
    n2 = random.randint(0, (i.size[1] - int(i.size[0] % len(s)) - 1) % 0xFFFF)
    '''
    n2 check the height of the message which is 1143
    i.size[0] is 1116 abd we check remainder for 5 which is 1 and we encrise it by 1 so it 0
    the remainder of 1143%0xFFFF is 1143
    andom.randint generate randome number between 0 and 1143
    '''

    do2(i.size, p, "".join([chr(j) for j in mb(n1, n2, len(s) & 0xFFFF)]), 0, 0, 0)
    

    x = ((((165 & 44 * 2) << 5) ^ 26) ^ 41) + 46
    do2(i.size, p, s, n1, n2, x)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=str, help='image file')
    parser.add_argument("string", type=str)
    parser.add_argument("out", type=str, help='png file')
    return parser.parse_args()


def main():
    args = parse_args()## add arguments to the script to make a command
    image = Image.open(args.image) ## take the input from the user on the agrument and open it
    do(image, args.string)
    image.save(args.out if args.out.endswith("png") else ".".join([args.out, "png"]))


if __name__ == "__main__":
    main() ##called to main function
