file = open("date.txt","w")
for k in range(1950,2021):
    k = str(k).rjust(4,"0")
    for i in range(1,13):
        i = str(i).rjust(2,"0")
        for j in range(1,32):
            j = str(j).rjust(2,"0")
            file.write(j+i+k+"\n")
file.close()

