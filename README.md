# locatecovid19
Attempt for locating possible Covid-19 infected people, using location history of confirmed infected person


# How to use:
  i. Assume that you are known infected person who uses google maps on her phone
  and download your location history.\
  ii. Have python3 with pandas and json library installed.\
       If not then follow this(for linux)\
       a. pip install pandas\
       b. pip install json\
  iii. Go to the link https://takeout.google.com/settings/takeout/custom/location_history\
       and download your location history. Unzip the archive and locate the file\
       Location History.json in the subfolder.\
  iv. Rename the file Location History.json to Location_History.json and put in\
      same directory as the script cutdata.py\
   v. Open file cutdata.py and adjust dates on line no. 55 the format is date,
      month, year\
   vi. Save and run python cutdata.py in terminal or as you wish.\
   vii. This will generate the file lochist.json\
   viii. Go to the site https://locationhistoryvisualizer.com/heatmap/ and
      it will give the map of locations where you have been most.\

Below is the screenshot of where did I spent my time during my last visit to my hometown Amgaon!

![alt text](https://github.com/hiteshvvr/locatecovid19/blob/master/image.png)

Now using the semantic location history, we can get the addresses. But because
the google addresses are many times wrong, it creats somewhat wieard problem.
For this \
    i. Save the semantic data of required month as semantic.json in the
    directory of addresses.py file.\
    ii. run python addresses.py \
    iii. It will generate the location data as before to be used with the
    location history visualizer website.\
    iv. Along with this it will create high risk, mid risk and low risk files as
    well in csv format, containing addresses.\
    v. If duration is less than 60 min its low risk, between 60 to 120 min its
    medium risk more than 120 mins high risk\

    As the address on google maps is not correct, it creats slightly wrong 
<<<<<<< HEAD
    but concise results, as shown in figure below:\

![alt text](https://github.com/hiteshvvr/locatecovid19/blob/master/image.png)
=======
    but concise results, as shown in figure below:
![alt text](https://github.com/hiteshvvr/locatecovid19/blob/master/image2.png)
>>>>>>> 507e26364d4a1c32aa1dd4c4a267c7ac192d223e
