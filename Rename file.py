from os import rename, listdir


badsufix = input("Enter the sufix to be removed : ")
fnames = listdir('.')

for fname in fnames:
    if fname.endswith(badsufix):
        rname = fname.replace(badsufix, "")
        print(rname)
        rname = rname+'.mkv'
        rename(fname, rname)
