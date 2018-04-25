import urllib

file = open("checking.txt", "w")
for lop in range(100000):
    link = "http://35.158.25.165/"+str(lop)
    f = urllib.urlopen(link)
    myfile = f.read()
    file.write("trying"+', '+str(lop)+', '+myfile+'\n')
    if myfile[0:5] != "Hello":
        print ("found!!!!!!!!!! ",lop,myfile,"!!!!!!!!!!!!!!!")
    else:
        print ("trying ",lop,myfile)