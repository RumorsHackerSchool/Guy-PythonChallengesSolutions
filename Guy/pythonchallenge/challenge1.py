string1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
string2 = list(string1)
abc = 'abcdefghijklnmopqrstvuwxyz'
def replace(letter):
    abc = list('abcdefghijklmnopqrstuvwxyz .\'()')
    cde = list('cdefghijklmnopqrstuvwxyzab .\'()')
    letter2 = cde[abc.index(letter)]
    return letter2

list1 = []
for letter in string1:
    list1.append(replace(letter))
print ''.join(list1)


