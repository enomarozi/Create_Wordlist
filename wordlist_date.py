bulan = {"01":"januari","02":"febuari","03":"maret","04":"april","05":"mei",
         "06":"juni","07":"juli","08":"agustus","09":"september","10":"oktober",
         "11":"november","12":"desember"}

file = open("date.txt","w")
for k in range(1950,2021):
    k = str(k).rjust(4,"0")
    for i in range(1,13):
        i = str(i).rjust(2,"0")
        for j in range(1,32):
            j = str(j).rjust(2,"0")
            file.write(j+i+k+"\n")
            if i in bulan.keys():
                file.write(j+bulan[i]+k+"\n")
for k in range(1950,2021):
    k = str(k).rjust(4,"0")
    for i in range(1,13):
        i = str(i).rjust(2,"0")
        for j in range(1,32):
            j = str(j).rjust(2,"0")
            file.write(i+j+k+"\n")
            if i in bulan.keys():
                file.write(bulan[i]+j+k+"\n")
file.close()

