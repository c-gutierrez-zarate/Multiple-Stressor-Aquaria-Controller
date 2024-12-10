#Import libraries
from decimal import Decimal
import RPi.GPIO as GPIO
import urllib.request 
import urllib.parse 
import sys
import os
import fcntl
import time
import copy
import io
import time      
import string     
import re
import pymysql
from AtlasI2C import (AtlasI2C)


time.sleep(2)#to give time to the database to initiate

mydb = pymysql.connect(
    host="localhost",
    user= "XXXX", #add info
    passwd="XXXX", #add info
    db="XXX" #add database name
    )

# Extract pH setpoints from the database 
mycursor_set_ph = mydb.cursor()
sql_set_ph = "SELECT * FROM set_ph"

mycursor_set_ph.execute(sql_set_ph)
myresult_set_ph = mycursor_set_ph.fetchall()

id,date,set_ph_T1,set_ph_T2,set_ph_T3,set_ph_T4,set_ph_T5,set_ph_T6,set_ph_T7,set_ph_T8,set_ph_C1,set_ph_C2 = myresult_set_ph[0]

print (myresult_set_ph[0]) #Print pH setpoints to see on the header at the start of the script

# Extract pH hysteresis values from the database
mycursor_his_ph = mydb.cursor()
sql_his_ph = "SELECT * FROM hist_ph"

mycursor_his_ph.execute(sql_his_ph)
myresult_his_ph = mycursor_his_ph.fetchall()

id,date,hist_ph_T1,hist_ph_T2,hist_ph_T3,hist_ph_T4,hist_ph_T5,hist_ph_T6,hist_ph_T7,hist_ph_T8,hist_ph_C1,hist_ph_C2 = myresult_his_ph[0]

print (myresult_his_ph[0])  #Print pH hysteresis to see on the header at the start of the script

# Extract DO (from now on, od) setpoints from the database 
mycursor_set_od = mydb.cursor()
sql_set_od = "SELECT * FROM set_od"

mycursor_set_od.execute(sql_set_od)
myresult_set_od = mycursor_set_od.fetchall()

id,date,set_od_T1,set_od_T2,set_od_T3,set_od_T4,set_od_T5,set_od_T6,set_od_T7,set_od_T8,set_od_C1,set_od_C2 = myresult_set_od[0]

print (myresult_set_od[0]) #Print od setpoints to see on the header at the start of the script

# Extract do hysteresis values from the database 
mycursor_his_od = mydb.cursor()
sql_his_od = "SELECT * FROM hist_od"

mycursor_his_od.execute(sql_his_od)
myresult_his_od = mycursor_his_od.fetchall()

id,date,hist_od_T1,hist_od_T2,hist_od_T3,hist_od_T4,hist_od_T5,hist_od_T6,hist_od_T7,hist_od_T8,hist_od_C1,hist_od_C2 = myresult_his_od[0]

print (myresult_his_od[0])  #Print od hysteresis values to see on the header at the start of the script

# Extract temperature calibration values from the database
mycursor_cal_temp_ph_od = mydb.cursor()
sql_cal_temp_ph_od = "SELECT * FROM cal_temp_ph_od"

mycursor_cal_temp_ph_od.execute(sql_cal_temp_ph_od)
myresult_cal_temp_ph_od = mycursor_cal_temp_ph_od.fetchall()

id,date,cal_temp_T1,cal_temp_T2,cal_temp_T3,cal_temp_T4,cal_temp_T5,cal_temp_T6,cal_temp_T7,cal_temp_T8, cal_temp_C1, cal_temp_C2 = myresult_cal_temp[0]

print (myresult_cal_temp_ph_od[0]) #Print calibration values of the temperature probes to see on the header at the start of the script

# Extract pH calibration values from the database
mycursor_cal_ph = mydb.cursor()
sql_cal_ph = "SELECT * FROM cal_ph"

mycursor_cal_ph.execute(sql_cal_ph)
myresult_cal_ph = mycursor_cal_ph.fetchall()

id,date,cal_ph_T1,cal_ph_T2,cal_ph_T3,cal_ph_T4,cal_ph_T5,cal_ph_T6,cal_ph_T7,cal_ph_T8,cal_ph_C1,cal_ph_C2 = myresult_cal_ph[0]

print (myresult_cal_ph[0]) #Print calibration values of the pH probes to see on the header at the start of the script

# Extract do (% sat) calibration values from the database
mycursor_cal_od = mydb.cursor()
sql_cal_od = "SELECT * FROM cal_od"

mycursor_cal_od.execute(sql_cal_od)
myresult_cal_od = mycursor_cal_od.fetchall()

id,date,cal_od_T1,cal_od_T2,cal_od_T3,cal_od_T4,cal_od_T5,cal_od_T6,cal_od_T7,cal_od_T8,cal_od_C1,cal_od_C2 = myresult_cal_od[0]

print (myresult_cal_od[0]) #Print calibration values of the od (% sat) probes to see on the header at the start of the script

# Extract do (mg/L) calibration values from the database
mycursor_cal_odmg = mydb.cursor()
sql_cal_odmg = "SELECT * FROM cal_od_mgl"

mycursor_cal_odmg.execute(sql_cal_odmg)
myresult_cal_odmg = mycursor_cal_odmg.fetchall()

id,date,cal_od_T1mg,cal_od_T2mg,cal_od_T3mg,cal_od_T4mg,cal_od_T5mg,cal_od_T6mg,cal_od_T7mg,cal_od_T8mg,cal_od_C1mg,cal_od_C2mg = myresult_cal_odmg[0]

print (myresult_cal_odmg[0]) #Print calibration values of the od (mg/L) probes to see on the header at the start of the script

# Function to extract data from each pH probe from every tank
def obtain_sonda_ph(tank):
    mycursor_sondas_ph = mydb.cursor()
    sql_sondas_ph = "SELECT tank, i2c FROM sondas WHERE tank = %s AND tipo = 'ph'"
    mycursor_sondas_ph.execute(sql_sondas_ph,(tank))
    myresult_sondas_ph = mycursor_sondas_ph.fetchone()
    print (myresult_sondas_ph[1])
    return (myresult_sondas_ph[1])

# Function to extract data from each od probe from every tank 
def obtain_sonda_od(tank):
    mycursor_sondas_od = mydb.cursor()
    sql_sondas_od = "SELECT tank, i2c FROM sondas WHERE tank = %s AND tipo = 'od'"
    mycursor_sondas_od.execute(sql_sondas_od,(tank))
    myresult_sondas_od = mycursor_sondas_od.fetchone()
    print (myresult_sondas_od[1])
    return (myresult_sondas_od[1])

# Function to extract data from temperature pH probe from every tank 
def obtain_sonda_temp(tank):
    mycursor_sondas_temp_ph_od = mydb.cursor()
    sql_sondas_temp_ph_od = "SELECT tank, num_serie FROM sondas WHERE tank = %s AND tipo = 'temp'"
    mycursor_sondas_temp_ph_od.execute(sql_sondas_temp_ph_od,(tank))
    myresult_sondas_temp_ph_od = mycursor_sondas_temp_ph_od.fetchone()
    print (myresult_sondas_temp_ph_od[1])
    return (myresult_sondas_temp_ph_od[1])

# Extract data from the pH probes from each tank
sondaphT1 = obtain_sonda_ph('T1')
sondaphT2 = obtain_sonda_ph('T2')
sondaphT3 = obtain_sonda_ph('T3')
sondaphT4 = obtain_sonda_ph('T4')
sondaphT5 = obtain_sonda_ph('T5')
sondaphT6 = obtain_sonda_ph('T6')
sondaphT7 = obtain_sonda_ph('T7')
sondaphT8 = obtain_sonda_ph('T8')
sondaphC1 = obtain_sonda_ph('C1')
sondaphC2 = obtain_sonda_ph('C2')

# Extract data from the do probes from each tank
sondaodT1 = obtain_sonda_od('T1')
sondaodT2 = obtain_sonda_od('T2')
sondaodT3 = obtain_sonda_od('T3')
sondaodT4 = obtain_sonda_od('T4')
sondaodT5 = obtain_sonda_od('T5')
sondaodT6 = obtain_sonda_od('T6')
sondaodT7 = obtain_sonda_od('T7')
sondaodT8 = obtain_sonda_od('T8')
sondaodC1 = obtain_sonda_od('C1')
sondaodC2 = obtain_sonda_od('C2')

# Extract data from the temperature probes from each tank
sondatempT1 = obtain_sonda_temp('T1')
sondatempT2 = obtain_sonda_temp('T2')
sondatempT3 = obtain_sonda_temp('T3')
sondatempT4 = obtain_sonda_temp('T4')
sondatempT5 = obtain_sonda_temp('T5')
sondatempT6 = obtain_sonda_temp('T6')
sondatempT7 = obtain_sonda_temp('T7')
sondatempT8 = obtain_sonda_temp('T8')
sondatempC1 = obtain_sonda_temp('C1')
sondatempC2 = obtain_sonda_temp('C2')

histphT1 = hist_ph_T1/2 # rename the pH hysteresis in T1 and divide in half
histphT2 = hist_ph_T2/2 # rename the pH hysteresis in T2 and divide in half
histphT3 = hist_ph_T3/2 # rename the pH hysteresis in T3 and divide in half
histphT4 = hist_ph_T4/2 # rename the pH hysteresis in T4 and divide in half
histphT5 = hist_ph_T5/2 # rename the pH hysteresis in T5 and divide in half
histphT6 = hist_ph_T6/2 # rename the pH hysteresis in T6 and divide in half
histphT7 = hist_ph_T7/2 # rename the pH hysteresis in T7 and divide in half
histphT8 = hist_ph_T8/2 # rename the pH hysteresis in T8 and divide in half
histphC1 = hist_ph_C1/2 # rename the pH hysteresis in C1 and divide in half
histphC2 = hist_ph_C2/2 # rename the pH hysteresis in C2 and divide in half

histodT1 = hist_od_T1/2 # rename the od hysteresis in T1 and divide in half
histodT2 = hist_od_T2/2 # rename the od hysteresis in T2 and divide in half
histodT3 = hist_od_T3/2 # rename the od hysteresis in T3 and divide in half
histodT4 = hist_od_T4/2 # rename the od hysteresis in T4 and divide in half
histodT5 = hist_od_T5/2 # rename the od hysteresis in T5 and divide in half
histodT6 = hist_od_T6/2 # rename the od hysteresis in T6 and divide in half
histodT7 = hist_od_T7/2 # rename the od hysteresis in T7 and divide in half
histodT8 = hist_od_T8/2 # rename the od hysteresis in T8 and divide in half
histodC1 = hist_od_C1/2 # rename the od hysteresis in C1 and divide in half
histodC2 = hist_od_C2/2 # rename the od hysteresis in C2 and divide in half

caltempT1 = cal_temp_T1 # rename temperature calibration in T1
caltempT2 = cal_temp_T2 # rename temperature calibration in T2
caltempT3 = cal_temp_T3 # rename temperature calibration in T3
caltempT4 = cal_temp_T4 # rename temperature calibration in T4
caltempT5 = cal_temp_T5 # rename temperature calibration in T5
caltempT6 = cal_temp_T6 # rename temperature calibration in T6
caltempT7 = cal_temp_T7 # rename temperature calibration in T7
caltempT8 = cal_temp_T8 # rename temperature calibration in T8
caltempC1 = cal_temp_C1 # rename temperature calibration in C1
caltempC2 = cal_temp_C2 # rename temperature calibration in C2

calphT1 = cal_ph_T1 # rename pH calibration in T1
calphT2 = cal_ph_T2 # rename pH calibration in T2
calphT3 = cal_ph_T3 # rename pH calibration in T3
calphT4 = cal_ph_T4 # rename pH calibration in T4
calphT5 = cal_ph_T5 # rename pH calibration in T5
calphT6 = cal_ph_T6 # rename pH calibration in T6
calphT7 = cal_ph_T7 # rename pH calibration in T7
calphT8 = cal_ph_T8 # rename pH calibration in T8
calphC1 = cal_ph_C1 # rename pH calibration in C1
calphC2 = cal_ph_C2 # rename pH calibration in C2

calodT1 = cal_od_T1 # rename od (% sat) calibration in T1
calodT2 = cal_od_T2 # rename od (% sat) calibration in T2
calodT3 = cal_od_T3 # rename od (% sat) calibration in T3
calodT4 = cal_od_T4 # rename od (% sat) calibration in T4
calodT5 = cal_od_T5 # rename od (% sat) calibration in T5
calodT6 = cal_od_T6 # rename od (% sat) calibration in T6
calodT7 = cal_od_T7 # rename od (% sat) calibration in T7
calodT8 = cal_od_T8 # rename od (% sat) calibration in T8
calodC1 = cal_od_C1 # rename od (% sat) calibration in C1
calodC2 = cal_od_C2 # rename od (% sat) calibration in C2


calodT1mg = cal_od_T1mg # rename od (mg/L) calibration in T1
calodT2mg = cal_od_T2mg # rename od (mg/L) calibration in T2
calodT3mg = cal_od_T3mg # rename od (mg/L) calibration in T3
calodT4mg = cal_od_T4mg # rename od (mg/L) calibration in T4
calodT5mg = cal_od_T5mg # rename od (mg/L) calibration in T5
calodT6mg = cal_od_T6mg # rename od (mg/L) calibration in T6
calodT7mg = cal_od_T7mg # rename od (mg/L) calibration in T7
calodT8mg = cal_od_T8mg # rename od (mg/L) calibration in T8
calodC1mg = cal_od_C1mg # rename od (mg/L) calibration in C1
calodC2mg = cal_od_C2mg # rename od (mg/L) calibration in C2



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(14, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(15, GPIO.OUT) # pin for the control of the relay module 
GPIO.setup(17, GPIO.OUT) # pin for the control of the relay module 
GPIO.setup(18, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(27, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(22, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(23, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(24, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(10, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(11, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(8, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(7, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(9, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(25, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(12, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(26, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(16, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(20, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(21, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(5, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(6, GPIO.OUT) # pin for the control of the relay module
GPIO.setup(13, GPIO.OUT) # pin for the control of the relay module 
GPIO.setup(19, GPIO.OUT) # pin for the control of the relay module

GPIO.output(14, True) # assign pin as output for pH1
GPIO.output(15, True) # assign pin as output for pH2
GPIO.output(17, True) # assign pin as output for pH3
GPIO.output(18, True) # assign pin as output for pH4
GPIO.output(27, True) # assign pin as output for pH5
GPIO.output(22, True) # assign pin as output for pH6
GPIO.output(23, True) # assign pin as output for pH7
GPIO.output(24, True) # assign pin as output for pH8
GPIO.output(10, True) # assign pin as output for pH9
GPIO.output(11, True) # assign pin as output for pH10
GPIO.output(8, True) # assign pin as output for od1
GPIO.output(7, True) # assign pin as output for od2
GPIO.output(9, True) # assign pin as output for od3
GPIO.output(25, True) # assign pin as output for od4
GPIO.output(12, True) # assign pin as output for od5
GPIO.output(26, True) # assign pin as output for od6
GPIO.output(16, True) # assign pin as output for od7
GPIO.output(20, True) # assign pin as output for od8
GPIO.output(21, True) # assign pin as output for od9
GPIO.output(5, True) # assign pin as output for od10
GPIO.output(6, True) # assign pin as output for pH
GPIO.output(13, True) # assign pin as output for od
GPIO.output(19, True) # assign pin as output for the reset of temperature probes

relePh1 = 0 #set default value to 0
relePh2 = 0 #set default value to 0
relePh3 = 0 #set default value to 0
relePh4 = 0 #set default value to 0
relePh5 = 0 #set default value to 0
relePh6 = 0 #set default value to 0
relePh7 = 0 #set default value to 0
relePh8 = 0 #set default value to 0
relePh9 = 0 #set default value to 0
relePh10 = 0 #set default value to 0

releOd1 = 0 #set default value to 0
releOd2 = 0 #set default value to 0
releOd3 = 0 #set default value to 0
releOd4 = 0 #set default value to 0
releOd5 = 0 #set default value to 0
releOd6 = 0 #set default value to 0
releOd7 = 0 #set default value to 0
releOd8 = 0 #set default value to 0
releOd9 = 0 #set default value to 0
releOd10 = 0 #set default value to 0

tr=0.5 #time of activation of relay module
GPIO.output(19, False)
time.sleep(3)
print ("------------------------ Reset of temperature probes -------------------")
GPIO.output(19, True)
time.sleep(2)

while True:
    try:
        print("---------------------------Reading temperatures...-------------------------")
        tempfileT1 = open("/sys/bus/w1/devices/"+ sondatempT1 +"/w1_slave")
        thetextT1 = tempfileT1.read()
        tempfileT1.close()
        tempT1data = thetextT1.split("\n")[1].split(" ")[9]
        temperatureT1 = float(tempT1data[2:])
        while (thetextT1.split("\n")[0].strip()[-3:] !='YES') or (thetextT1.split("\n")[1].strip()[-5:] > '30000'):
            time.sleep(2)
            print ("Retry reading T1")
            time.sleep(2)
            tempfileT1 = open("/sys/bus/w1/devices/"+sondatempT1+"/w1_slave")
            thetextT1 = tempfileT1.read()
            tempfileT1.close()
            tempT1data = thetextT1.split("\n")[1].split(" ")[9]
            temperatureT1 = float(tempT1data[2:])
            GPIO.output(19, False)
            time.sleep(3)
            print ("Reset of temperature probes")
            GPIO.output(19, True)
        temperatureT1 = temperatureT1 / 1000
        temperatureT1 = temperatureT1 + caltempT1 # to calibrate the temperature probe
        temperatureT1 = round(temperatureT1, 2) # round to 2 decimals
        print("T1:", temperatureT1)
        
        tempfileT2 = open("/sys/bus/w1/devices/"+ sondatempT2 +"/w1_slave")
        thetextT2 = tempfileT2.read()
        tempfileT2.close()
        tempT2data = thetextT2.split("\n")[1].split(" ")[9]
        temperatureT2 = float(tempT2data[2:])
        while (thetextT2.split("\n")[0].strip()[-3:] !='YES') or (thetextT2.split("\n")[1].strip()[-5:] > '30000'):
            time.sleep(2)
            #print (thetextT2.split("\n")[1].strip()[-5:])
            print ("Retry reading T2")
            time.sleep(2)
            tempfileT2 = open("/sys/bus/w1/devices/"+sondatempT2+"/w1_slave")
            thetextT2 = tempfileT2.read()
            tempfileT2.close()
            tempT2data = thetextT2.split("\n")[1].split(" ")[9]
            temperatureT2 = float(tempT2data[2:])
            #print (temperatureT2)
            GPIO.output(19, False)
            time.sleep(3)
            print ("Reset of temperature probes")
            GPIO.output(19, True)
        temperatureT2 = temperatureT2 / 1000
        temperatureT2 = temperatureT2 + caltempT2 # to calibrate the temperature probe
        temperatureT2 = round(temperatureT2, 2) # round to 2 decimals
        print("T2:", temperatureT2)
        
        tempfileT3 = open("/sys/bus/w1/devices/"+ sondatempT3 +"/w1_slave")
        thetextT3 = tempfileT3.read()
        tempfileT3.close()
        tempT3data = thetextT3.split("\n")[1].split(" ")[9]
        temperatureT3 = float(tempT3data[2:])
        #print (tempT3data)
        while (thetextT3.split("\n")[0].strip()[-3:] !='YES') or (thetextT3.split("\n")[1].strip()[-5:] > '30000'):
            time.sleep(2)
            #print (thetextT3.split("\n")[1].strip()[-5:])
            print ("Retry reading T3")
            time.sleep(2)
            tempfileT3 = open("/sys/bus/w1/devices/"+sondatempT3+"/w1_slave")
            thetextT3 = tempfileT3.read()
            tempfileT3.close()
            tempT3data = thetextT3.split("\n")[1].split(" ")[9]
            temperatureT3 = float(tempT3data[2:])
            #print (temperatureT3)
            GPIO.output(19, False)
            time.sleep(3)
            print ("Reset of temperature probes")
            GPIO.output(19, True)
        temperatureT3 = temperatureT3 / 1000
        temperatureT3 = temperatureT3 + caltempT3 # to calibrate the temperature probe
        temperatureT3 = round(temperatureT3, 2) # round to 2 decimals
        print("T3:", temperatureT3)
        
        tempfileT4 = open("/sys/bus/w1/devices/"+ sondatempT4 +"/w1_slave")
        thetextT4 = tempfileT4.read()
        tempfileT4.close()
        tempT4data = thetextT4.split("\n")[1].split(" ")[9]
        temperatureT4 = float(tempT4data[2:])
        while (thetextT4.split("\n")[0].strip()[-3:] !='YES') or (thetextT4.split("\n")[1].strip()[-5:] > '30000'):
            time.sleep(2)
            print ("Retry reading T4")
            time.sleep(2)
            tempfileT4 = open("/sys/bus/w1/devices/"+sondatempT4+"/w1_slave")
            thetextT4 = tempfileT4.read()
            tempfileT4.close()
            tempT4data = thetextT4.split("\n")[1].split(" ")[9]
            temperatureT4 = float(tempT4data[2:])
            GPIO.output(19, False)
            time.sleep(3)
            print ("Reset of temperature probes")
            GPIO.output(19, True)
        temperatureT4 = temperatureT4 / 1000
        temperatureT4 = temperatureT4  + caltempT4 # to calibrate the temperature probe
        temperatureT4 = round(temperatureT4, 2) # round to 2 decimals
        print("T4:", temperatureT4)
        
        tempfileT5 =open("/sys/bus/w1/devices/"+ sondatempT5 +"/w1_slave")
        thetextT5 = tempfileT5.read()
        tempfileT5.close()
        tempT5data = thetextT5.split("\n")[1].split(" ")[9]
        temperatureT5 = float(tempT5data[2:])
        while (thetextT5.split("\n")[0].strip()[-3:] !='YES') or (thetextT5.split("\n")[1].strip()[-5:] > '30000'):
            time.sleep(2)
            print ("Retry reading T5")
            time.sleep(2)
            tempfileT5 = open("/sys/bus/w1/devices/"+sondatempT5+"/w1_slave")
            thetextT5 = tempfileT5.read()
            tempfileT5.close()
            tempT5data = thetextT5.split("\n")[1].split(" ")[9]
            temperatureT5 = float(tempT5data[2:])
            GPIO.output(19, False)
            time.sleep(3)
            print ("Reset of temperature probes")
            GPIO.output(19, True)
        temperatureT5 = temperatureT5 / 1000
        temperatureT5 = temperatureT5  + caltempT5 # to calibrate the temperature probe
        temperatureT5 = round(temperatureT5, 2) # round to 2 decimals
        print("T5:", temperatureT5)
        
        tempfileT6 =open("/sys/bus/w1/devices/"+ sondatempT6+"/w1_slave")
        thetextT6 = tempfileT6.read()
        tempfileT6.close()
        tempT6data = thetextT6.split("\n")[1].split(" ")[9]
        temperatureT6 = float(tempT6data[2:])
        while (thetextT6.split("\n")[0].strip()[-3:] !='YES') or (thetextT6.split("\n")[1].strip()[-5:] > '30000'):
            time.sleep(2)
            print ("Retry reading T6")
            time.sleep(2)
            tempfileT6 = open("/sys/bus/w1/devices/"+sondatempT6+"/w1_slave")
            thetextT6 = tempfileT6.read()
            tempfileT6.close()
            tempT6data = thetextT6.split("\n")[1].split(" ")[9]
            temperatureT6 = float(tempT6data[2:])
            GPIO.output(19, False)
            time.sleep(3)
            print ("Reset of temperature probes")
            GPIO.output(19, True)    
        temperatureT6 = temperatureT6 / 1000
        temperatureT6 = temperatureT6 + caltempT6 # to calibrate the temperature probe
        temperatureT6 = round(temperatureT6, 2)  # round to 2 decimals
        print("T6:", temperatureT6)
        
        tempfileT7 =open("/sys/bus/w1/devices/"+ sondatempT7+"/w1_slave")
        thetextT7 = tempfileT7.read()
        tempfileT7.close()
        tempT7data = thetextT7.split("\n")[1].split(" ")[9]
        temperatureT7 = float(tempT7data[2:])
        while (thetextT7.split("\n")[0].strip()[-3:] !='YES') or (thetextT7.split("\n")[1].strip()[-5:] > '30000'):
            time.sleep(2)
            print ("Retry reading T7")
            time.sleep(2)
            tempfileT7 = open("/sys/bus/w1/devices/"+sondatempT7+"/w1_slave")
            thetextT7 = tempfileT7.read()
            tempfileT7.close()
            tempT7data = thetextT7.split("\n")[1].split(" ")[9]
            temperatureT7 = float(tempT7data[2:])
            GPIO.output(19, False)
            time.sleep(3)
            print ("Reset of temperature probes")
            GPIO.output(19, True)
        temperatureT7 = temperatureT7 / 1000
        temperatureT7 = temperatureT7 + caltempT7 # to calibrate the temperature probe
        temperatureT7 = round(temperatureT7, 2) # round to 2 decimals
        print("T7:", temperatureT7)
        
        tempfileT8 =open("/sys/bus/w1/devices/"+ sondatempT8 +"/w1_slave")
        thetextT8 = tempfileT8.read()
        tempfileT8.close()
        tempT8data = thetextT8.split("\n")[1].split(" ")[9]
        temperatureT8 = float(tempT8data[2:])
        while (thetextT8.split("\n")[0].strip()[-3:] !='YES') or (thetextT8.split("\n")[1].strip()[-5:] > '30000'):
            time.sleep(2)
            print ("Retry reading T8")
            time.sleep(2)
            tempfileT8 = open("/sys/bus/w1/devices/"+sondatempT8+"/w1_slave")
            thetextT8 = tempfileT8.read()
            tempfileT8.close()
            tempT8data = thetextT8.split("\n")[1].split(" ")[9]
            temperatureT8 = float(tempT8data[2:])
            GPIO.output(19, False)
            time.sleep(3)
            print ("Reset of temperature probes")
            GPIO.output(19, True)
        temperatureT8 = temperatureT8 / 1000
        temperatureT8 = temperatureT8 + caltempT8 # to calibrate the temperature probe
        temperatureT8 = round(temperatureT8, 2) # round to 2 decimals
        print("T8:", temperatureT8)
        
        tempfileT9 =open("/sys/bus/w1/devices/"+ sondatempC1 +"/w1_slave")
        thetextT9 = tempfileT9.read()
        tempfileT9.close()
        tempT9data = thetextT9.split("\n")[1].split(" ")[9]
        temperatureT9 = float(tempT9data[2:])
        while (thetextT9.split("\n")[0].strip()[-3:] !='YES') or (thetextT9.split("\n")[1].strip()[-5:] > '30000'):
            time.sleep(2)
            print ("Retry reading T9")
            time.sleep(2)
            tempfileT9 = open("/sys/bus/w1/devices/"+sondatempC1+"/w1_slave")
            thetextT9 = tempfileT9.read()
            tempfileT9.close()
            tempT9data = thetextT9.split("\n")[1].split(" ")[9]
            temperatureT9 = float(tempT9data[2:])
            GPIO.output(19, False)
            time.sleep(3)
            print ("Reset of temperature probes")
            GPIO.output(19, True)
        temperatureT9 = temperatureT9 / 1000
        temperatureT9 = temperatureT9 + caltempC1 # to calibrate the temperature probe
        temperatureT9 = round(temperatureT9, 2) # round to 2 decimals
        print("T9:", temperatureT9)
        
        tempfileT10 =open("/sys/bus/w1/devices/"+ sondatempC2 +"/w1_slave")
        thetextT10 = tempfileT10.read()
        tempfileT10.close()
        tempT10data = thetextT10.split("\n")[1].split(" ")[9]
        temperatureT10 = float(tempT10data[2:])
        while (thetextT10.split("\n")[0].strip()[-3:] !='YES') or (thetextT10.split("\n")[1].strip()[-5:] > '30000'):
            time.sleep(2)
            print ("Retry reading T10")
            time.sleep(2)
            tempfileT10 = open("/sys/bus/w1/devices/"+sondatempC2+"/w1_slave")
            thetextT10 = tempfileT10.read()
            tempfileT10.close()
            tempT10data = thetextT10.split("\n")[1].split(" ")[9]
            temperatureT10 = float(tempT10data[2:])
            GPIO.output(19, False)
            time.sleep(3)
            print ("Reset of temperature probes")
            GPIO.output(19, True)
        temperatureT10 = temperatureT10 / 1000
        temperatureT10 = temperatureT10 + caltempC2 # to calibrate the temperature probe
        temperatureT10 = round(temperatureT10, 2) # round to 2 decimals
        print("T10:", temperatureT10)
        
        # Extract I2C address of each pH and do probe
        device1 = AtlasI2C(int(sondaphT1))
        device2 = AtlasI2C(int(sondaphT2))
        device3 = AtlasI2C(int(sondaphT3))
        device4 = AtlasI2C(int(sondaphT4))
        device5 = AtlasI2C(int(sondaphT5))
        device6 = AtlasI2C(int(sondaphT6))
        device7 = AtlasI2C(int(sondaphT7))
        device8 = AtlasI2C(int(sondaphT8))
        device9 = AtlasI2C(int(sondaphC1))
        device10 = AtlasI2C(int(sondaphC2))
        device11 = AtlasI2C(int(sondaodT1))
        device12 = AtlasI2C(int(sondaodT2))
        device13 = AtlasI2C(int(sondaodT3))
        device14 = AtlasI2C(int(sondaodT4))
        device15 = AtlasI2C(int(sondaodT5))
        device16 = AtlasI2C(int(sondaodT6))
        device17 = AtlasI2C(int(sondaodT7))
        device18 = AtlasI2C(int(sondaodT8))
        device19 = AtlasI2C(int(sondaodC1))
        device20 = AtlasI2C(int(sondaodC2))
        
        print("-------------------------- Reading pH... ------------------------")
        
        t_read = (1)
        # extract pH1 value with temperature compensation
        Ph1 = device1.query('RT,' + str(temperatureT1))
        while Ph1.strip()[:7] != 'Success':
            Ph1 = device1.query('RT,' + str(temperatureT1))
            print(Ph1)
            print("Retry reading Ph1")
            time.sleep(t_read)
        Ph1 = Ph1[13:18]
        Ph1 = round(float(Ph1), 3) + calphT1 # to round to 3 decimals + apply calibration
        print("Ph1: ",Ph1)
        
        # extract pH2 value with temperature compensation
        Ph2 = device2.query('RT,' + str(temperatureT2))
        while Ph2.strip()[:7] != 'Success':
            Ph2 = device2.query('RT,' + str(temperatureT2))
            print(Ph2)
            print("Retry reading Ph2")
            time.sleep(t_read)
        Ph2 = Ph2[13:18]
        Ph2 = round(float(Ph2), 3) + calphT2 # to round to 3 decimals + apply calibration
        print("Ph2: ",Ph2)
        
        # extract pH3 value with temperature compensation
        Ph3 = device3.query('RT,' + str(temperatureT3))
        while Ph3.strip()[:7] != 'Success':
            Ph3 = device3.query('RT,' + str(temperatureT3))
            print(Ph3)
            print("Retry reading Ph3")
            time.sleep(t_read)
        Ph3 = Ph3[13:18]
        Ph3 = round(float(Ph3), 3) + calphT3 # to round to 3 decimals + apply calibration
        print("Ph3: ",Ph3)
        
        # extract pH4 value with temperature compensation
        Ph4 = device4.query('RT,' + str(temperatureT4))
        while Ph4.strip()[:7] != 'Success':
            Ph4 = device4.query('RT,' + str(temperatureT4))
            print(Ph4)
            print("Retry reading Ph4")
            time.sleep(t_read)
        Ph4 = Ph4[13:18]
        Ph4 = round(float(Ph4), 3) + calphT4 # to round to 3 decimals + apply calibration
        print("Ph4: ",Ph4)
          
        # extract pH5 value with temperature compensation
        Ph5 = device5.query('RT,' + str(temperatureT5))
        while Ph5.strip()[:7] != 'Success':
            Ph5 = device5.query('RT,' + str(temperatureT5))
            print(Ph5)
            print("Retry reading Ph5")
            time.sleep(t_read)
        Ph5 = Ph5[13:18]
        Ph5 = round(float(Ph5), 3) + calphT5 # to round to 3 decimals + apply calibration
        print("Ph5: ",Ph5)
        
        # extract pH6 value with temperature compensation
        Ph6 = device6.query('RT,' + str(temperatureT6))
        while Ph6.strip()[:7] != 'Success':
            Ph6 = device6.query('RT,' + str(temperatureT6))
            print(Ph6)
            print("Retry reading Ph6")
            time.sleep(t_read)
        Ph6 = Ph6[13:18]
        Ph6 = round(float(Ph6), 3) + calphT6 # to round to 3 decimals + apply calibration
        print("Ph6: ",Ph6)
        
        # extract pH7 value with temperature compensation
        Ph7 = device7.query('RT,' + str(temperatureT7))
        while Ph7.strip()[:7] != 'Success':
            Ph7 = device7.query('RT,' + str(temperatureT7))
            print(Ph7)
            print("Retry reading Ph7")
            time.sleep(t_read)
        Ph7 = Ph7[13:18]
        Ph7 = round(float(Ph7), 3) + calphT7 # to round to 3 decimals + apply calibration
        print("Ph7: ",Ph7)
        
        # extract pH8 value with temperature compensation
        Ph8 = device8.query('RT,' + str(temperatureT8))
        while Ph8.strip()[:7] != 'Success':
            Ph8 = device8.query('RT,' + str(temperatureT8))
            print(Ph8)
            print("Retry reading Ph8")
            time.sleep(t_read)
        Ph8 = Ph8[13:18]
        Ph8 = round(float(Ph8), 3) + calphT8 # to round to 3 decimals + apply calibration
        print("Ph8: ",Ph8)
        
        # extract pH9 value with temperature compensation
        Ph9 = device9.query('RT,' + str(temperatureT9))
        while Ph9.strip()[:7] != 'Success':
            Ph9 = device9.query('RT,' + str(temperatureT9))
            print(Ph9)
            print("Retry reading Ph9")
            time.sleep(t_read)
        Ph9 = Ph9[13:18]
        Ph9 = round(float(Ph9), 3) + calphC1 # to round to 3 decimals + apply calibration
        print("Ph9: ",Ph9)
        
        # extract pH10 value with temperature compensation
        Ph10 = device10.query('RT,' + str(temperatureT10))
        while Ph10.strip()[:7] != 'Success':
            Ph10 = device10.query('RT,' + str(temperatureT10))
            print(Ph10)
            print("Retry reading Ph10")
            time.sleep(t_read)
        Ph10 = Ph10[13:18]
        Ph10 = round(float(Ph10), 3) + calphC2 # to round to 3 decimals + apply calibration
        print("Ph10: ",Ph10)
        
        print("------------------------ Reading DO... --------------------------")
    
        # extract od1 value with temperature compensation
        Od1 = device11.query('RT,' + str(temperatureT1))
        while Od1.strip()[:7] != 'Success':
            Od1 = device11.query('RT,' + str(temperatureT1))
            print(Od1)
            print("Retry reading Od1")
            time.sleep(t_read)
        Od1mg = Od1[13:17] # mg/l
        Od1 = Od1[18:23] # %
        Od1 = Od1.replace("\x00","")
        Od1 = Od1.replace(",","")
        Od1 = round(float(Od1), 2) + calodT1 # to round to 2 decimals + apply calibration
        Od1mg = round(float(Od1mg), 2) + calodT1mg # to round to 2 decimals + apply calibration
        print("Od1: ",Od1)
        print("Od1mg: ",Od1mg)
        
        # extract od2 value with temperature compensation
        Od2 = device12.query('RT,' + str(temperatureT2))
        while Od2.strip()[:7] != 'Success':
            Od2 = device12.query('RT,' + str(temperatureT2))
            print(Od2)
            print("Retry reading Od2")
            time.sleep(t_read)
        Od2mg = Od2[13:17] # mg/l
        Od2 = Od2[18:23] # %
        Od2 = Od2.replace("\x00","")
        Od2 = Od2.replace(",","")
        Od2 = round(float(Od2), 2) + calodT2 # to round to 2 decimals + apply calibration
        Od2mg = round(float(Od2mg), 2) + calodT2mg # to round to 2 decimals + apply calibration
        print("Od2: ",Od2)
        print("Od2mg: ",Od2mg)
        
        # extract od3 value with temperature compensation
        Od3 = device13.query('RT,' + str(temperatureT3))
        while Od3.strip()[:7] != 'Success':
            Od3 = device13.query('RT,' + str(temperatureT3))
            print(Od3)
            print("Retry reading Od3")
            time.sleep(t_read)
        Od3mg = Od3[13:17] # mg/l
        Od3 = Od3[18:23] # %
        Od3 = Od3.replace("\x00","")
        Od3 = Od3.replace(",","")
        Od3 = round(float(Od3), 2) + calodT3 # to round to 2 decimals + apply calibration
        Od3mg = round(float(Od3mg), 2) + calodT3mg # to round to 2 decimals + apply calibration
        print("Od3: ",Od3)
        print("Od3mg: ",Od3mg)
        
        # extract od4 value with temperature compensation
        Od4 = device14.query('RT,' + str(temperatureT4))
        while Od4.strip()[:7] != 'Success':
            Od4 = device14.query('RT,' + str(temperatureT4))
            print(Od4)
            print("Retry reading Od4")
            time.sleep(t_read)
        Od4mg = Od4[13:17] # mg/l
        Od4 = Od4[18:23] # %
        Od4 = Od4.replace("\x00","")
        Od4 = Od4.replace(",","")        
        Od4 = round(float(Od4), 2) + calodT4 # to round to 2 decimals + apply calibration
        Od4mg = round(float(Od4mg), 2) + calodT4mg # to round to 2 decimals + apply calibration
        print("Od4: ",Od4)
        print("Od4mg: ",Od4mg)

        # extract od5 value with temperature compensation
        Od5 = device15.query('RT,' + str(temperatureT5))
        while Od5.strip()[:7] != 'Success':
            Od5 = device15.query('RT,' + str(temperatureT5))
            print(Od5)
            print("Retry reading Od5")
            time.sleep(t_read)
        Od5mg = Od5[13:17] # mg/l
        Od5 = Od5[18:23] # %
        Od5 = Od5.replace("\x00","")
        Od5 = Od5.replace(",","")        
        Od5 = round(float(Od5), 2) + calodT5 # to round to 2 decimals + apply calibration
        Od5mg = round(float(Od5mg), 2) + calodT5mg # to round to 2 decimals + apply calibration
        print("Od5: ",Od5)
        print("Od5mg: ",Od5mg)
        
        # extract od6 value with temperature compensation
        Od6 = device16.query('RT,' + str(temperatureT6))
        while Od6.strip()[:7] != 'Success':
            Od6 = device16.query('RT,' + str(temperatureT6))
            print(Od6)
            print("Retry reading Od6")
            time.sleep(t_read)
        Od6mg = Od6[13:17] # mg/l
        Od6 = Od6[18:23] # %
        Od6 = Od6.replace("\x00","")
        Od6 = Od6.replace(",","")        
        Od6 = round(float(Od6), 2) + calodT6 # to round to 2 decimals + apply calibration
        Od6mg = round(float(Od6mg), 2) + calodT6mg # to round to 2 decimals + apply calibration
        print("Od6: ",Od6)
        print("Od6mg: ",Od6mg)
        
        # extract od7 value with temperature compensation
        Od7 = device17.query('RT,' + str(temperatureT7))
        while Od7.strip()[:7] != 'Success':
            Od7 = device11.query('RT,' + str(temperatureT7))
            print(Od7)
            print("Retry reading Od7")
        Od7mg = Od7[13:17] # mg/l
        Od7 = Od7[18:23] # %
        Od7 = Od7.replace("\x00","")
        Od7 = Od7.replace(",","")        
        Od7 = round(float(Od7), 2) + calodT7 # to round to 2 decimals + apply calibration
        Od7mg = round(float(Od7mg), 2) + calodT7mg # to round to 2 decimals + apply calibration
        print("Od7: ",Od7)
        print("Od7mg: ",Od7mg)
        
        # extract od8 value with temperature compensation
        Od8 = device18.query('RT,' + str(temperatureT8))
        while Od8.strip()[:7] != 'Success':
            Od8 = device18.query('RT,' + str(temperatureT8))
            print(Od8)
            print("Retry reading Od8")
            time.sleep(t_read)
        Od8mg = Od8[13:17] # mg/l
        Od8 = Od8[18:23] # %
        Od8 = Od8.replace("\x00","")
        Od8 = Od8.replace(",","")
        print("Od8: ",Od8)
        print("Od8mg: ",Od8mg)
        Od8 = round(float(Od8), 2) + calodT8 # to round to 2 decimals + apply calibration
        Od8mg = round(float(Od8mg), 2) + calodT8mg # to round to 2 decimals + apply calibration
        print("Od8: ",Od8)
        print("Od8mg: ",Od8mg)
        
        # extract od9 value with temperature compensation
        Od9 = device19.query('RT,' + str(temperatureT9))
        while Od9.strip()[:7] != 'Success':
            Od9 = device19.query('RT,' + str(temperatureT9))
            print(Od9)
            print("Retry reading Od9")
            time.sleep(t_read)
        Od9mg = Od9[13:17] # mg/l
        Od9 = Od9[18:23] # %
        Od9 = Od9.replace("\x00","")
        Od9 = Od9.replace(",","")
        Od9 = round(float(Od9), 2) + calodC1 # to round to 2 decimals + apply calibration
        Od9mg = round(float(Od9mg), 2) + calodC1mg # to round to 2 decimals + apply calibration
        print("Od9: ",Od9)
        print("Od9a: ",Od9mg)
        
        # extract od10 value with temperature compensation
        Od10 = device20.query('RT,' + str(temperatureT10))
        while Od10.strip()[:7] != 'Success':
            Od10 = device20.query('RT,' + str(temperatureT10))
            print(Od10)
            print("Retry reading Od10")
            time.sleep(t_read)
        Od10mg = Od10[13:17] # mg/l
        Od10 = Od10[18:23] # %
        Od10 = Od10.replace("\x00","")
        Od10 = Od10.replace(",","")
        Od10 = round(float(Od10), 2) + calodC2 # to round to 2 decimals + apply calibration
        Od10mg = round(float(Od10mg), 2) + calodC2mg # to round to 2 decimals + apply calibration
        print("Od10: ",Od10)
        print("Od10mg: ",Od10mg)
        
        print("----------------------- Managing solenoid valves... ------------------------")
        
         # conditional to enable pin 14 (pH) to activate the relay module        
        if  ((Ph1 > (set_ph_T1 + histphT1) and relePh1 == 0) or ((Ph1 > (set_ph_T1 - histphT1)) and relePh1==1)):
            GPIO.output(14, False)
            print("RelePh1 activated, opening solenoid valve... Injecting CO2")
            relePh1=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(14, True)
            print("RelePh1 deactivated, closing solenoid vale...")
            relePh1=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time
            
          # conditional to enable pin 15 (pH) to activate the relay module     
        if  ((Ph2 > (set_ph_T2 + histphT2) and relePh2 == 0) or ((Ph2 > (set_ph_T2 - histphT2)) and relePh2==1)):
            GPIO.output(15, False)
            print("RelePh2 activated, opening solenoid valve... Injecting CO2")
            relePh2=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(15, True)
            print("RelePh2 deactivated, closing solenoid vale...")
            relePh2=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time

         # conditional to enable pin 17 (pH) to activate the relay module  
        if  ((Ph3 > (set_ph_T3 + histphT3) and relePh3 == 0) or ((Ph3 > (set_ph_T3 - histphT3)) and relePh1==1)):
            GPIO.output(17, False)
            print("RelePh3 activated, opening solenoid valve... Injecting CO2")
            relePh3=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(17, True)
            print("RelePh3 deactivated, closing solenoid vale...")
            relePh3=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time

         # conditional to enable pin 18 (pH) to activate the relay module  
        if  ((Ph4 > (set_ph_T4 + histphT4) and relePh4 == 0) or ((Ph4 > (set_ph_T4 - histphT4)) and relePh4==1)):
            GPIO.output(18, False)
            print("RelePh4 activated, opening solenoid valve... Injecting CO2")
            relePh4=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(18, True)
            print("RelePh4 deactivated, closing solenoid vale...")
            relePh4=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time

         # conditional to enable pin 27 (pH) to activate the relay module  
        if  ((Ph5 > (set_ph_T5 + histphT5) and relePh5 == 0) or ((Ph5 > (set_ph_T5 - histphT5)) and relePh5==1)):
            GPIO.output(27, False)
            print("RelePh5 activated, opening solenoid valve... Injecting CO2")
            relePh5=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(27, True)
            print("RelePh5 deactivated, closing solenoid vale...")
            relePh5=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time

         # conditional to enable pin 22 (pH) to activate the relay module  
        if  ((Ph6 > (set_ph_T6 + histphT6) and relePh6 == 0) or ((Ph6 > (set_ph_T6 - histphT6)) and relePh6==1)):
            GPIO.output(22, False)
            print("RelePh6 activated, opening solenoid valve... Injecting CO2")
            relePh6=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(22, True)
            print("RelePh6 deactivated, closing solenoid vale...")
            relePh6=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time

         # conditional to enable pin 23 (pH) to activate the relay module  
        if  ((Ph7 > (set_ph_T7 + histphT7) and relePh7 == 0) or ((Ph7 > (set_ph_T7 - histphT7)) and relePh7==1)):
            GPIO.output(23, False)
            print("RelePh7 activated, opening solenoid valve... Injecting CO2")
            relePh7=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(23, True)
            print("RelePh7 deactivated, closing solenoid vale...")
            relePh7=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time

         # conditional to enable pin 24 (pH) to activate the relay module  
        if  ((Ph8 > (set_ph_T8 + histphT8) and relePh8 == 0) or ((Ph8 > (set_ph_T8 - histphT8)) and relePh8==1)):
            GPIO.output(24, False)
            print("RelePh8 activated, opening solenoid valve... Injecting CO2")
            relePh8=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(24, True)
            print("RelePh8 deactivated, closing solenoid vale...")
            relePh8=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time

         # conditional to enable pin 10 (pH) to activate the relay module  
        if  ((Ph9 > (set_ph_C1 + histphC1) and relePh9 == 0) or ((Ph9 > (set_ph_C1 - histphC1)) and relePh9==1)):
            GPIO.output(10, False)
            print("RelePh9 activated, opening solenoid valve... Injecting CO2")
            relePh9=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(10, True)
            print("RelePh9 deactivated, closing solenoid vale...")
            relePh9=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time

         # conditional to enable pin 11 (pH) to activate the relay module  
        if  ((Ph10 > (set_ph_C2 + histphC2) and relePh10 == 0) or ((Ph10 > (set_ph_C2 - histphC2)) and relePh10==1)):
            GPIO.output(11, False)
            print("RelePh10 activated, opening solenoid valve... Injecting CO2")
            relePh10=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(11, True)
            print("RelePh10 deactivated, closing solenoid vale...")
            relePh10=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time
            
           
             # conditional to enable pin 8 (od) to activate the relay module 
        if  ((Od1 > (set_od_T1 + histodT1) and releOd1 == 0) or ((Od1 > (set_od_T1 - histodT1)) and releOd1==1)):
            GPIO.output(8, False)
            print("ReleOd1 activated, opening solenoid valve... Injecting N2")
            releOd1=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(8, True)
            print("ReleOd1 deactivated, closing solenoid vale...")
            releOd1=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time
            
            # conditional to enable pin 7 (od) to activate the relay module          
        if  ((Od2 > (set_od_T2 + histodT2) and releOd2 == 0) or ((Od2 > (set_od_T2 - histodT2)) and releOd2==1)):
            GPIO.output(7, False)
            print("ReleOd2 activated, opening solenoid valve... Injecting N2")
            releOd2=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(7, True)
            print("ReleOd2 deactivated, closing solenoid vale...")
            releOd2=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time
            
            # conditional to enable pin 9 (od) to activate the relay module          
        if  ((Od3 > (set_od_T3 + histodT3) and releOd3 == 0) or ((Od3 > (set_od_T3 - histodT3)) and releOd3==1)):
            GPIO.output(9, False)
            print("ReleOd3 activated, opening solenoid valve... Injecting N2")
            releOd3=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(9, True)
            print("ReleOd3 deactivated, closing solenoid vale...")
            releOd3=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time
            
            # conditional to enable pin 13 (od) to activate the relay module          
        if  ((Od4 > (set_od_T4 + histodT4) and releOd4 == 0) or ((Od4 > (set_od_T4 - histodT4)) and releOd4==1)):
            GPIO.output(13, False)
            print("ReleOd4 activated, opening solenoid valve... Injecting N2")
            releOd4=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(13, True)
            print("ReleOd4 deactivated, closing solenoid vale...")
            releOd4=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time
            
            # conditional to enable pin 12 (od) to activate the relay module           
        if  ((Od5 > (set_od_T5 + histodT5) and releOd5 == 0) or ((Od5 > (set_od_T5 - histodT5)) and releOd5==1)):
            GPIO.output(12, False)
            print("ReleOd5 activated, opening solenoid valve... Injecting N2")
            releOd5=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(12, True)
            print("ReleOd5 deactivated, closing solenoid vale...")
            releOd5=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time
            
            # conditional to enable pin 26 (od) to activate the relay module           
        if  ((Od6 > (set_od_T6 + histodT6) and releOd6 == 0) or ((Od6 > (set_od_T6 - histodT6)) and releOd6==1)):
            GPIO.output(26, False)
            print("ReleOd6 activated, opening solenoid valve... Injecting N2")
            releOd6=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(26, True)
            print("ReleOd6 deactivated, closing solenoid vale...")
            releOd6=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time
            
            # conditional to enable pin 16 (od) to activate the relay module           
        if  ((Od7 > (set_od_T7 + histodT7) and releOd7 == 0) or ((Od7 > (set_od_T7 - histodT7)) and releOd7==1)):
            GPIO.output(16, False)
            print("ReleOd7 activated, opening solenoid valve... Injecting N2")
            releOd7=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(16, True)
            print("ReleOd7 deactivated, closing solenoid vale...")
            releOd7=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time
            
           # conditional to enable pin 20 (od) to activate the relay module         
        if  ((Od8 > (set_od_T8 + histodT8) and releOd8 == 0) or ((Od8 > (set_od_T8 - histodT8)) and releOd8==1)):
            GPIO.output(20, False)
            print("ReleOd8 activated, opening solenoid valve... Injecting N2")
            releOd8=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(20, True)
            print("ReleOd8 deactivated, closing solenoid vale...")
            releOd8=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time
            
            # conditional to enable pin 21 (od) to activate the relay module         
        if  ((Od9 > (set_od_C1 + histodC1) and releOd9 == 0) or ((Od9 > (set_od_C1 - histodC1)) and releOd9==1)):
            GPIO.output(21, False)
            print("ReleOd9 activated, opening solenoid valve... Injecting N2")
            releOd9=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(21, True)
            print("ReleOd9 deactivated, closing solenoid vale...")
            releOd9=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time
            
            # conditional to enable pin 5 (od) to activate the relay module           
        if  ((Od10 > (set_od_C2 + histodC2) and releOd10 == 0) or ((Od10 > (set_od_C2 - histodC2)) and releOd10==1)):
            GPIO.output(5, False)
            print("ReleOd10 activated, opening solenoid valve... Injecting N2")
            releOd10=1 #reference of the activation of the relay
            time.sleep(tr) # solenoid valve opening pulse time
        else:
            GPIO.output(5, True)
            print("ReleOd10 deactivated, closing solenoid vale...")
            releOd10=0 #reference of the deactivation of the relay
            time.sleep(tr) # solenoid valve closing pulse time
            
        
        Lastdata = time.strftime('%c') #Lastdata = last data

        # Send data to text file where they are temporally stored until next reading
        fic = open("/var/www/html/ph_od/receptor_control.txt", "w")
        data = [str(Ph1), str(Ph2), str(Ph3),str(Ph4),str(Ph5),str(Ph6),str(Ph7),str(Ph8),str(Ph9),str(Ph10),str(Od1),str(Od2),str(Od3),str(Od4),str(Od5),str(Od6),str(Od7),str(Od8),str(Od9),str(Od10),str(relePh1),str(relePh2),str(relePh3),str(relePh4),str(relePh5),str(relePh6),str(relePh7),str(relePh8),str(relePh9),str(relePh10),str(releOd1),str(releOd2),str(releOd3),str(releOd4),str(releOd5),str(releOd6),str(releOd7),str(releOd8),str(releOd9),str(releOd10), str(Lastdata), str(temperatureT1), str(temperatureT2), str(temperatureT3), str(temperatureT4), str(temperatureT5), str(temperatureT6), str(temperatureT7), str(temperatureT8), str(temperatureT9), str(temperatureT10), str(Od1mg),str(Od2mg),str(Od3mg),str(Od4mg),str(Od5mg),str(Od6mg),str(Od7mg),str(Od8mg),str(Od9mg),str(Od10mg)]    

        for line in data:
            fic.write(line)
            fic.write("\n")
        
        fic.close()
        
        
        print ("Data sent to receptor text file" + time.strftime('%c'))  # display if the data have been successfully sent
        #print (data)
        print(" ")
        print("----------------  END OF READINGS  -------------------")
        print(" ")
     
# If any of these 3 errors occur, the system will reboot, displaying it on the screen
    except OSError as err:
        print("---------  OS error: {0}".format(err))
        print("Rebooting due to OSError")
        python = sys.executable
        os.execl(python, python, *sys.argv)
        
    except ValueError:
        print("Rebooting due to ValueError")
        python = sys.executable
        os.execl(python, python, *sys.argv)
        
    except IndexError:
        print("Rebooting due to IndexError")
        python = sys.executable
        os.execl(python, python, *sys.argv)



