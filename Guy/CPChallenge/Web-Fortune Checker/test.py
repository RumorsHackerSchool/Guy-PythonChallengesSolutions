import urllib
for lop in range(10000):
    link = "http://35.158.25.165/"+str(lop)
    f = urllib.urlopen(link)
    myfile = f.read()
    file = open("checking.txt", "w")
    file.write(myfile)
    if myfile[0:5] != "Hello":
        print ("found!!!!!!!!!! ",lop,myfile,"!!!!!!!!!!!!!!!")
    else:
        print ("trying ",lop,myfile)