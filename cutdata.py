import pandas as pd
import json
# import numpy as np
# import matplotlib.pyplot as plt
# from datetime import datetime as dt
# from mpl_toolkits.basemap import Basemap


# Read json format location data, and make dataframe
ldf = pd.read_json('Location_History.json')

# parse the data and cut only the range required.
def parsedf(ldf):
    ldf['timestamp_ms'] = ldf['locations'].map(lambda x: x['timestampMs'])
    ldf['datetime'] = ldf['timestamp_ms'].map(lambda x: pd.Timestamp(int(x), unit='ms'))
    ldf = ldf[(ldf['datetime']>pd.Timestamp(2019,11,1)) & (ldf['datetime']<pd.Timestamp(2019,11,30))]
    return ldf

# Make dict from dataframe.
def getdict(ldf):
    mlist =[]
    for index, row in ldf.iterrows():
        mlist.append(row['locations'])
    mdict = {"locations":mlist}
    return mdict
# Save as json from dict
def savejson(mdict):
    ajson = json.dumps(mdict)
    f = open("lochist.json","w")
    f.write(ajson)
    f.close()

ldf = parsedf(ldf)
mdict = getdict(ldf)
savejson(mdict)





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
