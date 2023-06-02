import requests
import datetime
import smtplib
import time

#---------ENTER YOUR EMAIL HERE---------#
myemail = "ENTER YOUR EMAIL HERE" 

#---------ENTER YOUR PASSWORD HERE---------#
mypwd = "ENTER YOUR PASSWORD HERE"

#---------ENTER YOUR COORDINATES HERE(REPLACE 1234)---------#
parameters = {
    "lat":1234,
    "lng":1234,
    "formatted":0
}

mylat = parameters['lat']
mylong = parameters['lng']

request = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
data = request.json()

issloc = requests.get(url="http://api.open-notify.org/iss-now.json")
dataloc = issloc.json()
isslat = float(dataloc['iss_position']['latitude'])
isslong = float(dataloc['iss_position']['longitude'])

#---------THE FOLLOWING SUNRISE AND SUNSET HOURS ARE CALCULATED IN IST, CHANGE AS PER YOUR TIME ZONE(CHANGE - 12 - 5.5 AND +5.5 ACCORDINGLY)---------#

sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0]) - 12 - 5.5
sunset = int(data['results']['sunset'].split("T")[1].split(":")[0]) + 5.5
timenow = datetime.datetime.now()
currenthour = timenow.hour


iscodeon = True
while iscodeon:

    if currenthour<sunrise or currenthour>sunset:
        if isslat in range(mylat-5,mylat+5) and isslong in range(mylong-5,mylong+5):
        
        #---------IF YOU WANT TO SEND THE EMAIL FROM A DIFFERENT DOMAIN, CHANGE "SMPT.GMAIL.COM" ACCORDINGLY.---------#
            with smtplib.SMTP("smpt.gmail.com") as connection:
                connection.starttls()
                connection.login(user=myemail,password=mypwd)
                #---------DO NOT FORGET TO CHANGE TARGET EMAIL ADDRESS---------#
                connection.sendmail(from_addr=myemail,to_addrs="TARGET EMAIL ADDRESS",msg="LOOK UP THE ISS IS ABOVE YOU")
    time.sleep(60)
