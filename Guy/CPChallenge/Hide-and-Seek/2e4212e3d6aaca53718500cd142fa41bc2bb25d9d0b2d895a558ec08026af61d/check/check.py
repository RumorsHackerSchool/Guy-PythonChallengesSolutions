def mb(*args):
    return [(args[int(i / 2)] >> ((i % 2) * 8)) & 0xff for i in range(len(args) * 2)]

print(mb(287, 1100, 5))