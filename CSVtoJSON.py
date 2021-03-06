import sys
from datetime import datetime, timedelta

import io
import math
import pandas as pd
import requests

alldata = {}

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
content = requests.get(url).content
confdata = pd.read_csv(io.StringIO(content.decode('utf-8')))

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
content = requests.get(url).content
deaddata = pd.read_csv(io.StringIO(content.decode('utf-8')))

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
content = requests.get(url).content
recvdata = pd.read_csv(io.StringIO(content.decode('utf-8')))

for days in range(1,1000):
    country = {}
    countrylist = []
    date = str(datetime.today() - timedelta(days=days))
    today = date[5:7] + "-" + date[8:10] + "-" + date[0:4]
    if today == "01-21-2020":
        break
    today = ""
    if date[5] == "0":
        today += date[6]
    else:
        today += date[5:7]
    today += "/"
    if date[8] == "0":
        today += date[9]
    else:
        today += date[8:10]
    today += "/" + date[2:4]
    print(today)

    for i in range(len(confdata.index)):
        name = confdata["Country/Region"][i]
        lat = confdata["Lat"][i]
        long = confdata["Long"][i]
        conf = confdata[today][i]
        if name not in country:
            country[name] = {"name": name, "lat": lat, "long": long, "conf": conf, "dead": 0, "recv": 0}
        else:
            country[name] = {"name": name, "lat": lat, "long": long, "conf": country[name]["conf"]+conf, "dead": 0, "recv": 0}

    for i in range(len(deaddata.index)):
        name = deaddata["Country/Region"][i]
        dead = deaddata[today][i]
        country[name]["dead"] += dead

    for i in range(len(recvdata.index)):
        name = recvdata["Country/Region"][i]
        recv = recvdata[today][i]
        country[name]["recv"] += recv

    country["Australia"]["lat"] = -25.2744
    country["Australia"]["long"] = 133.7751
    country["Canada"]["lat"] = 56.1304
    country["Canada"]["long"] = -106.3468
    country["China"]["lat"] = 35.8617
    country["China"]["long"] = 104.1954
    country["Denmark"]["lat"] = 56.2639
    country["Denmark"]["long"] = 9.5018
    country["France"]["lat"] = 46.2276
    country["France"]["long"] = 2.2137
    country["Netherlands"]["lat"] = 52.1326
    country["Netherlands"]["long"] = 5.2913
    country["United Kingdom"]["lat"] = 55.3781
    country["United Kingdom"]["long"] = -3.4360

    for i in country: countrylist += [country[i]]
    countrylist.sort(key=lambda s: s['conf'], reverse=True)
    alldata[today] = countrylist

fileout = open("timeseries.js", "w")
fileout.write("data = " + str(alldata))
fileout.close()

# End of tine series data collection
# Start of daily data collection

date = str(datetime.today() - timedelta(days=1))
today = date[5:7] + "-" + date[8:10] + "-" + date[0:4]
print(today)

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + today + ".csv"
content = requests.get(url).content
csv = pd.read_csv(io.StringIO(content.decode('utf-8')))

conflist = []
country = {}

for i in range(len(csv.index)):
    mname = str(csv["Admin2"][i])
    pname = str(csv["Province_State"][i])
    cname = str(csv["Country_Region"][i])
    if math.isnan(csv["Lat"][i]): lat = ""
    else: lat = csv["Lat"][i]
    if math.isnan(csv["Long_"][i]): lon = ""
    else: lon = csv["Long_"][i]
    conf = csv["Confirmed"][i]
    dead = csv["Deaths"][i]
    recv = csv["Recovered"][i]
    if math.isnan(csv["Active"][i]): active = 0
    else: active = csv["Active"][i]
    name = str(csv["Combined_Key"][i])
    try: rate = str(csv["Incidence_Rate"][i])
    except: rate = "N/A"
    try: cfr = str(csv["Case-Fatality_Ratio"][i])
    except: cfr = "N/A"
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

country["Australia"]["lat"] = -25.2744
country["Australia"]["lon"] = 133.7751
country["Australia"]["num"] = 1

country["Japan"]["lat"] = 36.2048
country["Japan"]["lon"] = 138.2529
country["Japan"]["num"] = 1

countrylist = []
for i in country:
    if country[i]["num"] != 0:
        country[i]["lat"] /= country[i]["num"]
        country[i]["lon"] /= country[i]["num"]
    countrylist += [country[i]]

conflist.sort(key=lambda s: s['conf'], reverse=True)
countrylist.sort(key=lambda s: s['conf'], reverse=True)

fileout = open("./data/"+today+".js", "w")
fileout.write("data = " + str(conflist))
fileout.close()

fileout = open("./data/"+today+"-country.js", "w")
fileout.write("data = " + str(countrylist))
fileout.close()

'''
alldata = {}

# countrylist = []
# date = str(datetime.today() - timedelta(days=1))
# today = date[5:7] + "-" + date[8:10] + "-" + date[0:4]
#
# url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + today + ".csv"
# content = requests.get(url).content
# csv = pd.read_csv(io.StringIO(content.decode('utf-8')))
#
# for i in range(len(csv.index)):
#     cname = str(csv["Country_Region"][i])
#     if cname in countrylist:
#         continue
#     if cname == "UK":
#         cname = "United Kingdom"
#     elif cname == "Mainland China":
#         cname = "China"
#     elif cname == "Russian Federation":
#         cname = "Russia"
#     elif cname == "South Korea":
#         cname = "Korea, South"
#     elif cname == "Republic of Korea":
#         cname = "Korea, South"
#     elif cname == "Iran (Islamic Republic of)":
#         cname = "Iran"
#     countrylist += [cname]
#
# print(str(countrylist))
#
# sys.exit()


date = str(datetime.today() - timedelta(days=1))
today = date[5:7] + "-" + date[8:10] + "-" + date[0:4]
print(today)

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + today + ".csv"
content = requests.get(url).content
csv = pd.read_csv(io.StringIO(content.decode('utf-8')))

conflist = []
country = {}

for i in range(len(csv.index)):
    mname = str(csv["Admin2"][i])
    # mname = "N/A"
    pname = str(csv["Province_State"][i])
    cname = str(csv["Country_Region"][i])
    if cname == "UK":
        cname = "United Kingdom"
    elif cname == "Mainland China":
        cname = "China"
    elif cname == "Russian Federation":
        cname = "Russia"
    elif cname == "South Korea":
        cname = "Korea, South"
    elif cname == "Republic of Korea":
        cname = "Korea, South"
    elif cname == "Iran (Islamic Republic of)":
        cname = "Iran"
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
    if math.isnan(csv["Active"][i]):
        active = 0
    else:
        active = csv["Active"][i]
    # active = "N/A"
    name = str(csv["Combined_Key"][i])
    # if pname != "":
    #     name = pname + ", " + cname
    # else:
    #     name = cname
    # rate = "N/A"
    # cfr = "N/A"
    try:
        rate = str(csv["Incidence_Rate"][i])
    except:
        rate = "N/A"
    try:
        cfr = str(csv["Case-Fatality_Ratio"][i])
    except:
        cfr = "N/A"
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

country["Australia"]["lat"] = -25.2744
country["Australia"]["lon"] = 133.7751
country["Australia"]["num"] = 1

country["Japan"]["lat"] = 36.2048
country["Japan"]["lon"] = 138.2529
country["Japan"]["num"] = 1

countrylist = []
for i in country:
    if country[i]["num"] != 0:
        country[i]["lat"] /= country[i]["num"]
        country[i]["lon"] /= country[i]["num"]
    countrylist += [country[i]]

conflist.sort(key=lambda s: s['conf'], reverse=True)
countrylist.sort(key=lambda s: s['conf'], reverse=True)

fileout = open("./data/"+today+".js", "w")
fileout.write("data = " + str(conflist))
fileout.close()

fileout = open("./data/"+today+"-country.js", "w")
fileout.write("data = " + str(countrylist))
fileout.close()

# sys.exit()

for days in range(1,200):
    date = str(datetime.today() - timedelta(days=days))
    today = date[5:7] + "-" + date[8:10] + "-" + date[0:4]
    if today == "03-21-2020":
        break
    print(date, days)

    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + today + ".csv"
    content = requests.get(url).content
    csv = pd.read_csv(io.StringIO(content.decode('utf-8')))

    conflist = []
    country = {}

    for i in range(len(csv.index)):
        mname = str(csv["Admin2"][i])
        # mname = "N/A"
        pname = str(csv["Province_State"][i])
        cname = str(csv["Country_Region"][i])
        if cname == "UK":
            cname = "United Kingdom"
        elif cname == "Mainland China":
            cname = "China"
        elif cname == "Russian Federation":
            cname = "Russia"
        elif cname == "South Korea":
            cname = "Korea, South"
        elif cname == "Republic of Korea":
            cname = "Korea, South"
        elif cname == "Iran (Islamic Republic of)":
            cname = "Iran"
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
        if math.isnan(csv["Active"][i]):
            active = 0
        else:
            active = csv["Active"][i]
        # active = "N/A"
        name = str(csv["Combined_Key"][i])
        # if pname != "":
        #     name = pname + ", " + cname
        # else:
        #     name = cname
        # rate = "N/A"
        # cfr = "N/A"
        try:
            rate = str(csv["Incidence_Rate"][i])
        except:
            rate = "N/A"
        try:
            cfr = str(csv["Case-Fatality_Ratio"][i])
        except:
            cfr = "N/A"
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

    country["Australia"]["lat"] = -25.2744
    country["Australia"]["lon"] = 133.7751
    country["Australia"]["num"] = 1

    country["Japan"]["lat"] = 36.2048
    country["Japan"]["lon"] = 138.2529
    country["Japan"]["num"] = 1

    countrylist = []
    for i in country:
        if country[i]["num"] != 0:
            country[i]["lat"] /= country[i]["num"]
            country[i]["lon"] /= country[i]["num"]
        countrylist += [country[i]]

    conflist.sort(key=lambda s: s['conf'], reverse=True)
    countrylist.sort(key=lambda s: s['conf'], reverse=True)

    # fileout = open("./data/"+today+".js", "w")
    # fileout.write("data = " + str(conflist))
    # fileout.close()
    #
    # fileout = open("./data/"+today+"-country.js", "w")
    # fileout.write("data = " + str(countrylist))
    # fileout.close()

    alldata[today] = countrylist

fileout = open("./countries/allcountrydata.js", "w")
fileout.write("data = " + str(alldata))
fileout.close()
'''

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