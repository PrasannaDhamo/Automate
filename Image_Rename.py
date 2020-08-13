from PIL import Image
import os
import datetime
import shutil

dates = set()
path = os.listdir("/Learning/img")
i = 1

for x in path:
    if x.endswith(".jpg"):
        age = Image.open(x)
        EXIF_data = age._getexif()
        if EXIF_data == None:
            print("No Data Found for " + x)
            age.close()
        else:
            dt = EXIF_data[306]
            dat = dt[0:10]
            dates_dash = dat.replace(":", "-")
            dates.add(dates_dash)
            age.close()
            rname = dates_dash +'.jpg'

        #if os.path.exists(rname) == False:
            #os.rename(x, rname)
        #else:
            #rname = dates_dash+"("+ str(i) +")"+'.jpg'
            #os.rename(x, rname)
            #i+=1

            rname = dates_dash+"("+ str(i) +")"+'.jpg'
            os.rename(x, rname)
            i+=1
        
            if not os.path.exists(dates_dash):
                os.mkdir(dates_dash)

path2 = os.listdir("/Learning/img")
for y in path2:
    for d in dates:
        if y.startswith(d):
            mov_dir = os.getcwd() + "\\" + d
            current_dir = os.getcwd() +  "\\" + y
            shutil.move(current_dir, mov_dir)

