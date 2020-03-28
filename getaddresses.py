import pandas as pd
import json
# import numpy as np
# import matplotlib.pyplot as plt
# from datetime import datetime as dt
# from mpl_toolkits.basemap import Basemap


# Read json format location data, and make dataframe
ldf = pd.read_json('data2019.json')

# parse the data and cut only the range required.
def parsedf(ldf):
    ldf['type'] = ldf['timelineObjects'].map(lambda x: list(x.keys())[0])
    ldf = ldf.query("type == 'placeVisit'")
    ldf['location'] = ldf['timelineObjects'].map(lambda x: x['placeVisit']['location'])
    ldf['time'] = ldf['timelineObjects'].map(lambda x: x['placeVisit']['duration'])
    ldf['duration'] = ldf['time'].map(lambda x: (int(x['endTimestampMs']) - int(x['startTimestampMs'])))/60000
    ldf['latitudeE7'] = ldf['location'].map(lambda x: x['latitudeE7'])
    ldf['longitudeE7'] = ldf['location'].map(lambda x: x['longitudeE7'])
    ldf['name'] = ldf['location'].map(lambda x: x['name'])
    ldf['addr'] = ldf['location'].map(lambda x: x['address'])
    ldf['timestampMs'] = ldf['time'].map(lambda x: x['startTimestampMs'])
    ldf['starttime'] = ldf['time'].map(lambda x: pd.Timestamp(int(x['startTimestampMs']), unit='ms'))
    ldf['endtime'] = ldf['time'].map(lambda x: pd.Timestamp(int(x['endTimestampMs']), unit='ms'))
    ldf = ldf[(ldf['starttime']>pd.Timestamp(2019,11,1)) & (ldf['starttime']<pd.Timestamp(2019,11,30))]
    return ldf

# Function to append to the list.
def mapp(llist, row):
    llist.append({"timestampMs" : row['timestampMs'],
                  "latitudeE7" : row['latitudeE7'],
                  "longitudeE7" : row['longitudeE7'],
                  "name" : row['name']})
    return llist


# Make dict from dataframe.
def getdict(ldf):
    llist =[]
    ldf_low = ldf.query('duration<60')
    ldf_med = ldf.query('duration>60 and duration<120')
    ldf_high = ldf.query('duration>120')

    for index, row in ldf_low.iterrows():
        llist = mapp(llist, row)
    for index, row in ldf_low.iterrows():
        for i in range(5):
            llist = mapp(llist, row)
    for index, row in ldf_low.iterrows():
        for i in range(15):
            llist = mapp(llist, row)
    
    ldict = {"locations":llist}
    ldf_low = ldf_low.drop(columns=['timelineObjects', 'type', 'location', 'time', 'timestampMs'])
    ldf_med = ldf_med.drop(columns=['timelineObjects', 'type', 'location', 'time', 'timestampMs'])
    ldf_high = ldf_high.drop(columns=['timelineObjects', 'type', 'location', 'time', 'timestampMs'])

    return ldict, ldf_low, ldf_med, ldf_high

# Save as json from dict
def saveall(ldict, ldf_low, ldf_med, ldf_high):
    ajson = json.dumps(ldict)
    f = open("addresshist.json","w")
    f.write(ajson)
    f.close()
    ldf_high.to_csv (r'high.csv', index = False, header=True)
    ldf_med.to_csv (r'med.csv', index = False, header=True)
    ldf_low.to_csv (r'low.csv', index = False, header=True)

ldf = parsedf(ldf)
ldict, ldf_low, ldf_med, ldf_high = getdict(ldf)
saveall(ldict, ldf_low, ldf_med, ldf_high)





# ===============================
# ldf['lat'] = ldf['locations'].map(lambda x: x['latitudeE7'])
# ldf['lon'] = ldf['locations'].map(lambda x: x['longitudeE7'])

# convert lat/lon to decimalized degrees and the timestamp to date-time
# ldf['lat'] = ldf['lat'] / 10.**7
# ldf['lon'] = ldf['lon'] / 10.**7
# ldf['timestamp_ms'] = ldf['timestamp_ms'].astype(float) / 1000
# ldf['datetime'] = ldf['timestamp_ms'].map(lambda x: datetime.datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
# ldf['datetime'] = ldf['timestamp_ms'].map(lambda x: datetime.datetime.fromtimestamp(x))
# date_range = '{}-{}'.format(ldf['datetime'].min()[:4], ldf['datetime'].max()[:4])
