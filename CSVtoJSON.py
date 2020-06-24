import pandas as pd
import requests, io, math
from datetime import datetime, timedelta

date = str(datetime.today() - timedelta(days=1))
today = date[5:7] + "-" + date[8:10] + "-" + date[0:4]

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + today + ".csv"
content = requests.get(url).content
csv = pd.read_csv(io.StringIO(content.decode('utf-8')))

conflist = []
country = {}

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
    if cname not in country:
        if lat == "":
            country[cname] = {"name": cname, "lat": 0, "lon": 0, "conf": conf, "dead": dead, "recv": recv, "active": active, "num": 0}
        else:
            country[cname] = {"name": cname, "lat": lat, "lon": lon, "conf": conf, "dead": dead, "recv": recv, "active": active, "num": 1}
    else:
        if lat == "":
            country[cname] = {"name": cname, "lat": country[cname]["lat"], "lon": country[cname]["lon"],
                              "conf": country[cname]["conf"] + conf, "dead": country[cname]["dead"] + dead,
                              "recv": country[cname]["recv"] + recv, "active": country[cname]["active"] + active,
                              "num": country[cname]["num"]}
        else:
            country[cname] = {"name": cname, "lat": country[cname]["lat"] + lat, "lon": country[cname]["lon"] + lon,
                              "conf": country[cname]["conf"] + conf, "dead": country[cname]["dead"] + dead,
                              "recv": country[cname]["recv"] + recv, "active": country[cname]["active"] + active,
                              "num": country[cname]["num"] + 1}

country["US"]["lat"] = 39.8283
country["US"]["lon"] = -98.5795
country["US"]["num"] = 1

country["Canada"]["lat"] = 56.1304
country["Canada"]["lon"] = -106.3468
country["Canada"]["num"] = 1

country["United Kingdom"]["lat"] = 55.3781
country["United Kingdom"]["lon"] = -3.4360
country["United Kingdom"]["num"] = 1

country["Netherlands"]["lat"] = 52.1326
country["Netherlands"]["lon"] = 5.2913
country["Netherlands"]["num"] = 1

country["France"]["lat"] = 46.2276
country["France"]["lon"] = 2.2137
country["France"]["num"] = 1

country["Denmark"]["lat"] = 56.2639
country["Denmark"]["lon"] = 9.5018
country["Denmark"]["num"] = 1

country["China"]["lat"] = 35.8617
country["China"]["lon"] = 104.1954
country["China"]["num"] = 1

country["Russia"]["lat"] = 61.5240
country["Russia"]["lon"] = 105.3188
country["Russia"]["num"] = 1

country["India"]["lat"] = 20.5937
country["India"]["lon"] = 78.9629
country["India"]["num"] = 1

countrylist = []
for i in country:
    if country[i]["num"] != 0:
        country[i]["lat"] /= country[i]["num"]
        country[i]["lon"] /= country[i]["num"]
    countrylist += [country[i]]

conflist.sort(key=lambda s: s['conf'], reverse=True)
countrylist.sort(key=lambda s: s['conf'], reverse=True)

fileout = open(today+".js", "w")
fileout.write("data = " + str(conflist))
fileout.close()

fileout = open(today+"-country.js", "w")
fileout.write("data = " + str(countrylist))
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