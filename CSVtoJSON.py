import pandas as pd
import requests, io, math
from datetime import datetime, timedelta

date = str(datetime.today() - timedelta(days=1))
today = date[5:7] + "-" + date[8:10] + "-" + date[0:4]

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + today + ".csv"
content = requests.get(url).content
csv = pd.read_csv(io.StringIO(content.decode('utf-8')))

conflist = []

for i in range(len(csv.index)):
    mname = str(csv["Admin2"][i])
    pname = str(csv["Province_State"][i])
    cname = str(csv["Country_Region"][i])
    if math.isnan(csv["Lat"][i]):
        lat = ""
    else:
        lat = csv["Lat"][i]
    if math.isnan(csv["Long_"][i]):
        lon = ""
    else:
        lon = csv["Long_"][i]
    conf = csv["Confirmed"][i]
    dead = csv["Deaths"][i]
    recv = csv["Recovered"][i]
    active = csv["Active"][i]
    name = str(csv["Combined_Key"][i])
    rate = str(csv["Incidence_Rate"][i])
    cfr = str(csv["Case-Fatality_Ratio"][i])
    conflist.append({"mname": mname, "pname": pname, "cname": cname, "lat": lat, "lon": lon, "conf": conf, "dead": dead, "recv": recv, "active": active, "name": name, "rate": rate, "cfr": cfr})

conflist.sort(key=lambda s: s['conf'], reverse=True)

fileout = open(today+".js", "w")
fileout.write("data = " + str(conflist))
fileout.close()

'''
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

fileout = open(today+".js", "w")
fileout.write("data = " + str(conflist))
fileout.close()
'''