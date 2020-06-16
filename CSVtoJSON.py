fileobj = open("06-15-2020.csv", "r") # r, w, a (read, write, append) are the available options
fileobj.readline()
datalist = fileobj.readlines()
fileobj.close()

conflist = []

for country in datalist:
    templist = country.split(",")
    pname = templist[2]
    cname = templist[3]
    lat = templist[5]
    lon = templist[6]
    conf = int(templist[7])
    conflist.append({"pname": pname, "cname": cname, "lat": lat, "lon": lon, "conf": conf})

conflist.sort(key=lambda s: s['conf'], reverse=True)

print(conflist)

fileout = open("06-15-2020.js", "w")
fileout.write("data = " + str(conflist))
fileout.close()
