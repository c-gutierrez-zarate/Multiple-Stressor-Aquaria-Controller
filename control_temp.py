#Import libraries
import decimal
import RPi.GPIO as GPIO
import io
import time       
import string     
import re
import pymysql
import os
import sys

print ("Waiting 2 seconds for system reboot")
time.sleep(2)

mydb = pymysql.connect(
    host='localhost',
    user= 'XXXX', #add info
    passwd='XXXX', #add info
    db='XXX' #add database name
    )

# Extract temperature setpoints from the database
mycursor_set_temp = mydb.cursor()
sql_set_temp = "SELECT * FROM set_temp"

mycursor_set_temp.execute(sql_set_temp)
myresult_set_temp = mycursor_set_temp.fetchall()

id,date,set_temp_T1,set_temp_T2,set_temp_T3,set_temp_T4,set_temp_T5,set_temp_T6,set_temp_T7,set_temp_T8,set_temp_BM1,set_temp_BM2,set_temp_BM3,set_temp_BM4,set_temp_BM5 = myresult_set_temp[0]

print (myresult_set_temp[0]) #Print temperature setpoints to see on the header at the start of the script

# Extract temperature hysteresis values from the database
mycursor_his_temp = mydb.cursor()
sql_his_temp = "SELECT * FROM hist_temp"

mycursor_his_temp.execute(sql_his_temp)
myresult_his_temp = mycursor_his_temp.fetchall()

id,date,hist_temp_T1,hist_temp_T2,hist_temp_T3,hist_temp_T4,hist_temp_T5,hist_temp_T6,hist_temp_T7,hist_temp_T8,hist_temp_BM1,hist_temp_BM2,hist_temp_BM3,hist_temp_BM4,hist_temp_BM5 = myresult_his_temp[0]

print (myresult_his_temp[0]) #Print temperature hysteresis to see on the header at the start of the script

# Extract temperature calibration values from the database
mycursor_cal_temp = mydb.cursor()
sql_cal_temp = "SELECT * FROM cal_temp"

mycursor_cal_temp.execute(sql_cal_temp)
myresult_cal_temp = mycursor_cal_temp.fetchall()

id,date,cal_temp_T1,cal_temp_T2,cal_temp_T3,cal_temp_T4,cal_temp_T5,cal_temp_T6,cal_temp_T7,cal_temp_T8,cal_temp_BM1,cal_temp_BM1_negro,cal_temp_BM1_blanco,cal_temp_BM2,cal_temp_BM2_rojo,cal_temp_BM2_azul,cal_temp_BM3,cal_temp_BM3_negro,cal_temp_BM3_blanco,cal_temp_BM4,cal_temp_BM4_rojo,cal_temp_BM4_azul,cal_temp_Agua, cal_temp_Room, cal_temp_BM5, cal_temp_Cap = myresult_cal_temp[0]

print (myresult_cal_temp[0]) #Print calibration values of the temperature probes to see on the header at the start of the script

# Function to extract data from each temperature probe from every tank
def obtain_sonda(tank):
    mycursor_sondas_temp = mydb.cursor()
    sql_sondas_temp = "SELECT tank, num_serie FROM sondas_temp WHERE tank = %s"
    mycursor_sondas_temp.execute(sql_sondas_temp,(tank))
    myresult_sondas_temp = mycursor_sondas_temp.fetchone()
    print (myresult_sondas_temp[1])
    return (myresult_sondas_temp[1])

# Extract data from the temperature probes from each tank
sondaT1 = obtain_sonda('T1')
sondaT2 = obtain_sonda('T2')
sondaT3 = obtain_sonda('T3')
sondaT4 = obtain_sonda('T4')
sondaT5 = obtain_sonda('T5')
sondaT6 = obtain_sonda('T6')
sondaT7 = obtain_sonda('T7')
sondaT8 = obtain_sonda('T8')
sondaBM1 = obtain_sonda('BM1')
sondaBM1_negro = obtain_sonda('BM1_negro')
sondaBM1_blanco = obtain_sonda('BM1_blanco')
sondaBM2 = obtain_sonda('BM2')
sondaBM2_rojo = obtain_sonda('BM2_rojo')
sondaBM2_azul = obtain_sonda('BM2_azul')
sondaBM3 = obtain_sonda('BM3')
sondaBM3_negro = obtain_sonda('BM3_negro')
sondaBM3_blanco = obtain_sonda('BM3_blanco')
sondaBM4 = obtain_sonda('BM4')
sondaBM4_rojo = obtain_sonda('BM4_rojo')
sondaBM4_azul = obtain_sonda('BM4_azul')
sondaAgua = obtain_sonda('Agua')
sondaRoom = obtain_sonda('Room')
sondaBM5 = obtain_sonda('BM5')
sondaCap = obtain_sonda('Cap')

histtempT1 = hist_temp_T1/2 # rename temperature hysteresis in T1 and divide in half
histtempT2 = hist_temp_T2/2 # rename temperature hysteresis in T2 and divide in half
histtempT3 = hist_temp_T3/2 # rename temperature hysteresis in T3 and divide in half
histtempT4 = hist_temp_T4/2 # rename temperature hysteresis in T4 and divide in half
histtempT5 = hist_temp_T5/2 # rename temperature hysteresis in T5 and divide in half
histtempT6 = hist_temp_T6/2 # rename temperature hysteresis in T6 and divide in half
histtempT7 = hist_temp_T7/2 # rename temperature hysteresis in T7 and divide in half
histtempT8 = hist_temp_T8/2 # rename temperature hysteresis in T8 and divide in half
histtempBM1tank = hist_temp_BM1/2 # rename temperature hysteresis in BM1 and divide in half
histtempBM2tank = hist_temp_BM2/2 # rename temperature hysteresis in BM2 and divide in half
histtempBM3tank = hist_temp_BM3/2 # rename temperature hysteresis in BM3 and divide in half
histtempBM4tank = hist_temp_BM4/2 # rename temperature hysteresis in BM4 and divide in half
histtempBM5tank = hist_temp_BM5/2 # rename temperature hysteresis in BM5 and divide in half

calT1 = cal_temp_T1 # rename temperature calibration in T1
calT2 = cal_temp_T2 # rename temperature calibration in T2
calT3 = cal_temp_T3 # rename temperature calibration in T3
calT4 = cal_temp_T4 # rename temperature calibration in T4
calT5 = cal_temp_T5 # rename temperature calibration in T5
calT6 = cal_temp_T6 # rename temperature calibration in T6
calT7 = cal_temp_T7 # rename temperature calibration in T7
calT8 = cal_temp_T8 # rename temperature calibration in T8
calBM1tank = cal_temp_BM1 # rename temperature calibration in BM1tank
calBM1negro = cal_temp_BM1_negro # rename temperature calibration in BM1negro
calBM1blanco = cal_temp_BM1_blanco # rename temperature calibration in BM1blanco
calBM2tank = cal_temp_BM2 # rename temperature calibration in BM2tank
calBM2rojo = cal_temp_BM2_rojo # rename temperature calibration in BM2rojo
calBM2azul = cal_temp_BM2_azul # rename temperature calibration in BM2azul
calBM3tank = cal_temp_BM3 # rename temperature calibration in BM3tank
calBM3negro = cal_temp_BM3_negro # rename temperature calibration in BM3negro
calBM3blanco = cal_temp_BM3_blanco # rename temperature calibration in BM3blanco
calBM4tank = cal_temp_BM4 # rename temperature calibration in BM4tank
calBM4rojo = cal_temp_BM4_rojo # rename temperature calibration in BM4rojo
calBM4azul = cal_temp_BM4_azul # rename temperature calibration in BM4azul
calTagua = cal_temp_Agua # rename temperature calibration in input water of the aquaria system
calTRoom = cal_temp_Room # rename temperature calibration in room
calBM5tank = cal_temp_BM5 # rename temperature calibration in BM5tank
calTcap = cal_temp_Cap # rename temperature calibration in input water of the life support system

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT) # pin for T1
GPIO.setup(18, GPIO.OUT) # pin for T2
GPIO.setup(27, GPIO.OUT) # pin for BM1 tank
GPIO.setup(22, GPIO.OUT) # pin for T3
GPIO.setup(23, GPIO.OUT) # pin for T4
GPIO.setup(24, GPIO.OUT) # pin for BM2 tank
GPIO.setup(25, GPIO.OUT) # pin for T5
GPIO.setup(12, GPIO.OUT) # pin for T6
GPIO.setup(26, GPIO.OUT) # pin for BM3 tank
GPIO.setup(16, GPIO.OUT) # pin for T7
GPIO.setup(20, GPIO.OUT) # pin for T8
GPIO.setup(21, GPIO.OUT) # pin for BM4 tank
GPIO.setup(5, GPIO.OUT) # pin for the reset of temperature probes
GPIO.setup(6, GPIO.OUT) # pin for BM5

GPIO.output(17, False) # assign pin as output for T1
GPIO.output(18, False) # assign pin as output for T2
GPIO.output(27, False) # assign pin as output for BM1 tank
GPIO.output(22, False) # assign pin as output for T3
GPIO.output(23, False) # assign pin as output for T4
GPIO.output(24, False) # assign pin as output for BM2tank
GPIO.output(25, False) # assign pin as output for T5
GPIO.output(12, False) # assign pin as output for T6
GPIO.output(26, True) # assign pin as output for BM3 tank
GPIO.output(16, True) # assign pin as output for T7
GPIO.output(20, True) # assign pin as output for T8
GPIO.output(21, True) # assign pin as output for BM4 tank
GPIO.output(6, True) # assign pin as output for BM5
GPIO.output(5, True) # assign pin as output for the reset of temperature probes

releT1 = 0 #set default value to 0
releT2 = 0 #set default value to 0
releT3 = 0 #set default value to 0
releT4 = 0 #set default value to 0
releT5 = 0 #set default value to 0
releT6 = 0 #set default value to 0
releT7 = 0 #set default value to 0
releT8 = 0 #set default value to 0
releBM1tank = 0 #set default value to 0
releBM2tank = 0 #set default value to 0
releBM3tank = 0 #set default value to 0
releBM4tank = 0 #set default value to 0
releBM5tank = 0 #set default value to 0

GPIO.setup(5, GPIO.OUT) # pin to reset power supply to probes (reset 1wire)
GPIO.output(5, False)        
time.sleep(2)
GPIO.output(5, False) # low output pulse to reset 1wire
print ("Probe reset")
time.sleep(2)
GPIO.output(5, True) # high output pulse to reset 1wire
print ("Probe reset OK")
print ("Iniciando lecturas")

time.sleep(0.5)

while True:
    try:
        ts=2 #  waiting time before retrying to read
        print(" ")
        print("--------------------------------------------------------------")
        print ("Data at " + time.strftime('%c'))  # display on the screen if data have been successfully sent  
        print("--------------------------------------------------------------")
    
        # Reading temperature in T1
        tempfileT1 = open("/sys/bus/w1/devices/"+sondaT1 + "/w1_slave")
        thetextT1 = tempfileT1.read()
        tempfileT1.close()
        while thetextT1.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)
            print ("Reading retry of temperature probe in T1")
            time.sleep(ts)
            thetextT1.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(ts)
            tempfileT1 = open("/sys/bus/w1/devices/"+ sondaT1 +"/w1_slave")
            thetextT1 = tempfileT1.read()
            tempfileT1.close()
        tempT1data = thetextT1.split("\n")[1].split(" ")[9]
        temperatureT1 = float(tempT1data[2:])
        temperatureT1 = temperatureT1 / 1000
        temperatureT1 = temperatureT1 + calT1 # calibration
        temperatureT1 = round(temperatureT1, 2) # round to 2 decimals
        print ("T1:", temperatureT1, "ºC")
    

        # Reading temperature in T2
        tempfileT2 = open("/sys/bus/w1/devices/"+ sondaT2 +"/w1_slave")
        thetextT2 = tempfileT2.read()
        tempfileT2.close()
        while thetextT2.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)
            print ("Reading retry of temperature probe in T2")
            time.sleep(ts)
            tempfileT2 = open("/sys/bus/w1/devices/"+ sondaT2 +"/w1_slave")
            thetextT2 = tempfileT2.read()
            tempfileT2.close()    
        tempT2data = thetextT2.split("\n")[1].split(" ")[9]
        temperatureT2 = float(tempT2data[2:])
        temperatureT2 = temperatureT2 / 1000
        temperatureT2 = temperatureT2 + calT2 # calibration
        temperatureT2 = round(temperatureT2, 2) # round to 2 decimals
        print ("T2:", temperatureT2, "ºC")

        # Reading temperature in T3
        tempfileT3 = open("/sys/bus/w1/devices/"+ sondaT3 +"/w1_slave")
        thetextT3 = tempfileT3.read()
        tempfileT3.close()
        while thetextT3.split("\n")[0].strip()[-3:] !='YES':
             time.sleep(2)     
             print ("Reading retry of temperature probe in T3")
             time.sleep(ts)
             tempfileT3 = open("/sys/bus/w1/devices/"+ sondaT3 +"/w1_slave")
             thetextT3 = tempfileT3.read()
             tempfileT3.close()
        tempT3data = thetextT3.split("\n")[1].split(" ")[9]
        temperatureT3 = float(tempT3data[2:])
        temperatureT3 = temperatureT3 / 1000
        temperatureT3 = temperatureT3 + calT3 # calibration
        temperatureT3 = round(temperatureT3, 2) # round to 2 decimals
        print ("T3:", temperatureT3, "ºC")

        # Reading temperature in T4
        tempfileT4 = open("/sys/bus/w1/devices/"+ sondaT4 +"/w1_slave")
        thetextT4 = tempfileT4.read()
        tempfileT4.close()
        while thetextT4.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)
            print ("Reading retry of temperature probe in T4")
            time.sleep(ts)
            tempfileT4 = open("/sys/bus/w1/devices/"+ sondaT4 +"/w1_slave")
            thetextT4 = tempfileT4.read()
            tempfileT4.close()    
        tempT4data = thetextT4.split("\n")[1].split(" ")[9]
        temperatureT4 = float(tempT4data[2:])
        temperatureT4 = temperatureT4 / 1000
        temperatureT4 = temperatureT4 + calT4 # calibration
        temperatureT4 = round(temperatureT4, 2) # round to 2 decimals
        print ("T4:", temperatureT4, "ºC")


        # Reading temperature in T5
        tempfileT5 = open("/sys/bus/w1/devices/"+ sondaT5 +"/w1_slave")
        thetextT5 = tempfileT5.read()
        tempfileT5.close()
        while thetextT5.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)
            print ("Reading retry of temperature probe in T5")
            time.sleep(ts)
            tempfileT5 = open("/sys/bus/w1/devices/"+ sondaT5 +"/w1_slave")
            thetextT5 = tempfileT5.read()
            tempfileT5.close()    
        tempT5data = thetextT5.split("\n")[1].split(" ")[9]
        temperatureT5 = float(tempT5data[2:])
        temperatureT5 = temperatureT5 / 1000
        temperatureT5 = temperatureT5 + calT5 # calibration
        temperatureT5 = round(temperatureT5, 2) # round to 2 decimals
        print ("T5:", temperatureT5, "ºC")

        # Reading temperature in T6
        tempfileT6 = open("/sys/bus/w1/devices/"+ sondaT6 +"/w1_slave")
        thetextT6 = tempfileT6.read()
        tempfileT6.close()
        while thetextT6.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)
            print ("Reading retry of temperature probe in T6")
            time.sleep(ts)
            tempfileT6 = open("/sys/bus/w1/devices/"+ sondaT6 +"/w1_slave")
            thetextT6 = tempfileT6.read()
            tempfileT6.close()    
        tempT6data = thetextT6.split("\n")[1].split(" ")[9]
        temperatureT6 = float(tempT6data[2:])
        temperatureT6 = temperatureT6 / 1000
        temperatureT6 = temperatureT6 + calT6 # calibration
        temperatureT6 = round(temperatureT6, 2) # round to 2 decimals
        print ("T6:", temperatureT6, "ºC")

        # Reading temperature in T7
        tempfileT7 = open("/sys/bus/w1/devices/"+ sondaT7 +"/w1_slave")
        thetextT7 = tempfileT7.read()
        tempfileT7.close()
        while thetextT7.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)     
            print ("Reading retry of temperature probe in T7")
            time.sleep(ts)
            tempfileT7 = open("/sys/bus/w1/devices/"+ sondaT7 +"/w1_slave")
            thetextT7 = tempfileT7.read()
            tempfileT7.close()    
        tempT7data = thetextT7.split("\n")[1].split(" ")[9]
        temperatureT7 = float(tempT7data[2:])
        temperatureT7 = temperatureT7 / 1000
        temperatureT7 = temperatureT7 + calT7 # calibration
        temperatureT7 = round(temperatureT7, 2) # round to 2 decimals
        print ("T7:", temperatureT7, "ºC")
        
        # Reading temperature in T8
        tempfileT8 = open("/sys/bus/w1/devices/"+ sondaT8 +"/w1_slave")
        thetextT8 = tempfileT8.read()
        tempfileT8.close()
        while thetextT8.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)
            print ("Reading retry of temperature probe in T8")
            time.sleep(ts)
            tempfileT8 = open("/sys/bus/w1/devices/"+ sondaT8 +"/w1_slave")
            thetextT8 = tempfileT8.read()
            tempfileT8.close()    
        tempT8data = thetextT8.split("\n")[1].split(" ")[9]
        temperatureT8 = float(tempT8data[2:])
        temperatureT8 = temperatureT8 / 1000
        temperatureT8 = temperatureT8 + calT8 # calibration
        temperatureT8 = round(temperatureT8, 2) # round to 2 decimals
        print ("T8:", temperatureT8, "ºC")

        # Reading temperature in BM1 tank
        tempfileBM1tank = open("/sys/bus/w1/devices/"+ sondaBM1 +"/w1_slave")
        thetextBM1tank = tempfileBM1tank.read()
        tempfileBM1tank.close()
        while thetextBM1tank.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)
            print ("Reading retry of temperature probe in BM1tank")
            time.sleep(ts)
            tempfileBM1tank = open("/sys/bus/w1/devices/"+ sondaBM1 +"/w1_slave")
            thetextBM1tank = tempfileBM1tank.read()
            tempfileBM1tank.close()    
        tempBM1tankdata = thetextBM1tank.split("\n")[1].split(" ")[9]
        temperatureBM1tank = float(tempBM1tankdata[2:])
        temperatureBM1tank = temperatureBM1tank / 1000
        temperatureBM1tank = temperatureBM1tank + calBM1tank # calibration
        temperatureBM1tank = round(temperatureBM1tank, 2) # round to 2 decimals
        print ("BM1:", temperatureBM1tank, "ºC")
          

        # Reading temperature in BM1 blanco
        tempfileBM1blanco = open("/sys/bus/w1/devices/"+ sondaBM1_blanco +"/w1_slave")
        thetextBM1blanco = tempfileBM1blanco.read()
        tempfileBM1blanco.close()
        while thetextBM1blanco.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)
            print ("Reading retry of temperature probe in BM1blanco")
            time.sleep(ts)
            tempfileBM1blanco = open("/sys/bus/w1/devices/"+ sondaBM1_blanco +"/w1_slave")
            thetextBM1blanco = tempfileBM1blanco.read()
            tempfileBM1blanco.close()     
        tempBM1blancodata = thetextBM1blanco.split("\n")[1].split(" ")[9]
        temperatureBM1blanco = float(tempBM1blancodata[2:])
        temperatureBM1blanco = temperatureBM1blanco / 1000
        temperatureBM1blanco = temperatureBM1blanco + calBM1blanco # calibration
        temperatureBM1blanco = round(temperatureBM1blanco, 2) # round to 2 decimals
        print ("BM1blanco:", temperatureBM1blanco, "ºC")

        
        
        # Reading temperature in BM1 negro
        tempfileBM1negro = open("/sys/bus/w1/devices/"+ sondaBM1_negro +"/w1_slave")
        thetextBM1negro = tempfileBM1negro.read()
        tempfileBM1negro.close()
        while thetextBM1negro.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)
            print ("Reading retry of temperature probe in BM1negro")
            time.sleep(ts)
            tempfileBM1negro = open("/sys/bus/w1/devices/"+ sondaBM1_negro +"/w1_slave")
            thetextBM1negro = tempfileBM1negro.read()
            tempfileBM1negro.close()      
        tempBM1negrodata = thetextBM1negro.split("\n")[1].split(" ")[9]
        temperatureBM1negro = float(tempBM1negrodata[2:])
        temperatureBM1negro = temperatureBM1negro / 1000
        temperatureBM1negro = temperatureBM1negro + calBM1negro # calibration
        temperatureBM1negro = round(temperatureBM1negro, 2) # round to 2 decimals
        print ("BM1negro:", temperatureBM1negro, "ºC")
           
        

        # Reading temperature in BM2 tank
        tempfileBM2tank = open("/sys/bus/w1/devices/"+ sondaBM2 +"/w1_slave")
        thetextBM2tank = tempfileBM2tank.read()
        tempfileBM2tank.close()
        while thetextBM2tank.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)
            print ("Reading retry of temperature probe in BM2tank")
            time.sleep(ts)
            tempfileBM2tank = open("/sys/bus/w1/devices/"+ sondaBM2 +"/w1_slave")
            thetextBM2tank = tempfileBM2tank.read()
            tempfileBM2tank.close()     
        tempBM2tankdata = thetextBM2tank.split("\n")[1].split(" ")[9]
        temperatureBM2tank = float(tempBM2tankdata[2:])
        temperatureBM2tank = temperatureBM2tank / 1000
        temperatureBM2tank = temperatureBM2tank + calBM2tank # calibration
        temperatureBM2tank = round(temperatureBM2tank, 2) # round to 2 decimals
        print ("BM2:", temperatureBM2tank, "ºC")

        # Reading temperature in BM2 rojo
        tempfileBM2rojo = open("/sys/bus/w1/devices/"+ sondaBM2_rojo +"/w1_slave")
        thetextBM2rojo = tempfileBM2rojo.read()
        tempfileBM2rojo.close()
        while thetextBM2rojo.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)
            print ("Reading retry of temperature probe in BM2rojo")
            time.sleep(ts)
            tempfileBM2rojo = open("/sys/bus/w1/devices/"+ sondaBM2_rojo +"/w1_slave")
            thetextBM2rojo = tempfileBM2rojo.read()
            tempfileBM2rojo.close()    
        tempBM2rojodata = thetextBM2rojo.split("\n")[1].split(" ")[9]
        temperatureBM2rojo = float(tempBM2rojodata[2:])
        temperatureBM2rojo = temperatureBM2rojo / 1000
        temperatureBM2rojo = temperatureBM2rojo + calBM2rojo # calibration
        temperatureBM2rojo = round(temperatureBM2rojo, 2) # round to 2 decimals
        print ("BM2rojo:", temperatureBM2rojo, "ºC")

        # Reading temperature in BM2 azul
        tempfileBM2azul = open("/sys/bus/w1/devices/"+ sondaBM2_azul +"/w1_slave")
        thetextBM2azul = tempfileBM2azul.read()
        tempfileBM2azul.close()
        while thetextBM2azul.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)    
            print ("Reading retry of temperature probe in BM2azul")
            time.sleep(ts)
            tempfileBM2azul = open("/sys/bus/w1/devices/"+ sondaBM2_azul +"/w1_slave")
            thetextBM2azul = tempfileBM2azul.read()
            tempfileBM2azul.close()      
        tempBM2azuldata = thetextBM2azul.split("\n")[1].split(" ")[9]
        temperatureBM2azul = float(tempBM2azuldata[2:])
        temperatureBM2azul = temperatureBM2azul / 1000
        temperatureBM2azul = temperatureBM2azul + calBM2azul # calibration
        temperatureBM2azul = round(temperatureBM2azul, 2) # round to 2 decimals
        print ("BM2azul:", temperatureBM2azul, "ºC")
        
        
        # Reading temperature in BM3 tank
        tempfileBM3tank = open("/sys/bus/w1/devices/"+ sondaBM3 +"/w1_slave")
        thetextBM3tank = tempfileBM3tank.read()
        tempfileBM3tank.close()
        while thetextBM3tank.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2) 
            print ("Reading retry of temperature probe in BM3tank")
            time.sleep(ts)
            tempfileBM3tank = open("/sys/bus/w1/devices/"+ sondaBM3 +"/w1_slave")
            thetextBM3tank = tempfileBM3tank.read()
            tempfileBM3tank.close()      
        tempBM3tankdata = thetextBM3tank.split("\n")[1].split(" ")[9]
        temperatureBM3tank = float(tempBM3tankdata[2:])
        temperatureBM3tank = temperatureBM3tank / 1000
        temperatureBM3tank = temperatureBM3tank + calBM3tank # calibration
        temperatureBM3tank = round(temperatureBM3tank, 2) # round to 2 decimals
        print ("BM3:", temperatureBM3tank, "ºC")

        # Reading temperature in BM3 blanco
        tempfileBM3blanco = open("/sys/bus/w1/devices/"+ sondaBM3_blanco +"/w1_slave")
        thetextBM3blanco = tempfileBM3blanco.read()
        tempfileBM3blanco.close()
        while thetextBM3blanco.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)
            print ("Reading retry of temperature probe in BM3blanco")
            time.sleep(ts)
            tempfileBM3blanco = open("/sys/bus/w1/devices/"+ sondaBM3_blanco +"/w1_slave")
            thetextBM3blanco = tempfileBM3blanco.read()
            tempfileBM3blanco.close()     
        tempBM3blancodata = thetextBM3blanco.split("\n")[1].split(" ")[9]
        temperatureBM3blanco = float(tempBM3blancodata[2:])
        temperatureBM3blanco = temperatureBM3blanco / 1000
        temperatureBM3blanco = temperatureBM3blanco + calBM3blanco # calibration
        temperatureBM3blanco = round(temperatureBM3blanco, 2) # round to 2 decimals
        print ("BM3blanco:", temperatureBM3blanco, "ºC")   

        # Reading temperature in BM3 negro
        tempfileBM3negro = open("/sys/bus/w1/devices/"+ sondaBM3_negro +"/w1_slave")
        thetextBM3negro = tempfileBM3negro.read()
        tempfileBM3negro.close()
        while thetextBM3negro.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)   
            print ("Reading retry of temperature probe in BM3negro")
            time.sleep(ts)
            tempfileBM3negro = open("/sys/bus/w1/devices/"+ sondaBM3_negro +"/w1_slave")
            thetextBM3negro = tempfileBM3negro.read()
            tempfileBM3negro.close()     
        tempBM3negrodata = thetextBM3negro.split("\n")[1].split(" ")[9]
        temperatureBM3negro = float(tempBM3negrodata[2:])
        temperatureBM3negro = temperatureBM3negro / 1000
        temperatureBM3negro = temperatureBM3negro + calBM3negro # calibration
        temperatureBM3negro = round(temperatureBM3negro, 2) # round to 2 decimals
        print ("BM3negro:", temperatureBM3negro, "ºC")   

        # Reading temperature in BM4 tank
        tempfileBM4tank = open("/sys/bus/w1/devices/"+ sondaBM4 +"/w1_slave")
        thetextBM4tank = tempfileBM4tank.read()
        tempfileBM4tank.close()
        while thetextBM4tank.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)
            print ("Reading retry of temperature probe in BM4tank")
            time.sleep(ts)
            tempfileBM4tank = open("/sys/bus/w1/devices/"+ sondaBM4 +"/w1_slave")
            thetextBM4tank = tempfileBM4tank.read()
            tempfileBM4tank.close()     
        tempBM4tankdata = thetextBM4tank.split("\n")[1].split(" ")[9]
        temperatureBM4tank = float(tempBM4tankdata[2:])
        temperatureBM4tank = temperatureBM4tank / 1000
        temperatureBM4tank = temperatureBM4tank + calBM4tank # calibration
        temperatureBM4tank = round(temperatureBM4tank, 2) # round to 2 decimals
        print ("BM4:", temperatureBM4tank, "ºC")

        # Reading temperature in BM4 rojo
        tempfileBM4rojo = open("/sys/bus/w1/devices/"+ sondaBM4_rojo +"/w1_slave")
        thetextBM4rojo = tempfileBM4rojo.read()
        tempfileBM4rojo.close()
        while thetextBM4rojo.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)
            print ("Reading retry of temperature probe in BM4rojo")
            time.sleep(ts)
            tempfileBM4rojo = open("/sys/bus/w1/devices/"+ sondaBM4_rojo +"/w1_slave")
            thetextBM4rojo = tempfileBM4rojo.read()
            tempfileBM4rojo.close()     
        tempBM4rojodata = thetextBM4rojo.split("\n")[1].split(" ")[9]
        temperatureBM4rojo = float(tempBM4rojodata[2:])
        temperatureBM4rojo = temperatureBM4rojo / 1000
        temperatureBM4rojo = temperatureBM4rojo + calBM4rojo # calibration
        temperatureBM4rojo = round(temperatureBM4rojo, 2) # round to 2 decimals
        print ("BM4rojo:", temperatureBM4rojo, "ºC")

        # Reading temperature in BM4 azul
        tempfileBM4azul = open("/sys/bus/w1/devices/"+ sondaBM4_azul +"/w1_slave")
        thetextBM4azul = tempfileBM4azul.read()
        tempfileBM4azul.close()
        while thetextBM4azul.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)
            print ("Reading retry of temperature probe in BM4azul")
            time.sleep(ts)
            tempfileBM4azul = open("/sys/bus/w1/devices/"+ sondaBM4_azul +"/w1_slave")
            thetextBM4azul = tempfileBM4azul.read()
            tempfileBM4azul.close()
        tempBM4azuldata = thetextBM4azul.split("\n")[1].split(" ")[9]
        temperatureBM4azul = float(tempBM4azuldata[2:])
        temperatureBM4azul = temperatureBM4azul / 1000
        temperatureBM4azul = temperatureBM4azul + calBM4azul # calibration
        temperatureBM4azul = round(temperatureBM4azul, 2) # round to 2 decimals
        print ("BM4azul:", temperatureBM4azul, "ºC")
        
        
        # Reading temperature in the room
        tempfileTRoom = open("/sys/bus/w1/devices/"+ sondaRoom +"/w1_slave")
        thetextTRoom = tempfileTRoom.read()
        tempfileTRoom.close()
        while thetextTRoom.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)    
            print ("Reading retry of temperature probe in room")
            time.sleep(0.5)
            tempfileTRoom = open("/sys/bus/w1/devices/"+ sondaRoom +"/w1_slave")
            thetextTRoom = tempfileTRoom.read()
            tempfileTRoom.close()
        tempTRoomdata = thetextTRoom.split("\n")[1].split(" ")[9]
        temperatureTRoom = float(tempTRoomdata[2:])
        temperatureTRoom = temperatureTRoom / 1000
        temperatureTRoom = temperatureTRoom + calTRoom # calibration
        temperatureTRoom = round(temperatureTRoom, 2) # round to 2 decimals
        print ("TRoom:", temperatureTRoom, "ºC")
        
        # Reading temperature in supply water of the aquaria system
        tempfileTagua = open("/sys/bus/w1/devices/"+ sondaAgua +"/w1_slave")
        thetextTagua = tempfileTagua.read()
        tempfileTagua.close()
        while thetextTagua.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)      
            print ("Reading retry of temperature probe in supply water of aquaria system")
            time.sleep(0.5)
            tempfileTagua = open("/sys/bus/w1/devices/"+ sondaAgua +"/w1_slave")
            thetextTagua = tempfileTagua.read()
            tempfileTagua.close()
        tempTaguadata = thetextTagua.split("\n")[1].split(" ")[9]
        temperatureTagua = float(tempTaguadata[2:])
        temperatureTagua = temperatureTagua / 1000
        temperatureTagua = temperatureTagua + calTagua # calibration
        temperatureTagua = round(temperatureTagua, 2) # round to 2 decimals
        print ("Tagua:", temperatureTagua, "ºC")
        
        # Reading temperature in BM5 tank
        tempfileBM5tank = open("/sys/bus/w1/devices/"+ sondaBM5 +"/w1_slave")
        thetextBM5tank = tempfileBM5tank.read()
        tempfileBM5tank.close()
        while thetextBM5tank.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)
            print ("Reading retry of temperature probe in BM5tank")
            time.sleep(ts)
            tempfileBM5tank = open("/sys/bus/w1/devices/"+ sondaBM5 +"/w1_slave")
            thetextBM5tank = tempfileBM5tank.read()
            tempfileBM5tank.close()     
        tempBM5tankdata = thetextBM5tank.split("\n")[1].split(" ")[9]
        temperatureBM5tank = float(tempBM5tankdata[2:])
        temperatureBM5tank = temperatureBM5tank / 1000
        temperatureBM5tank = temperatureBM5tank + calBM5tank # calibration
        temperatureBM5tank = round(temperatureBM5tank, 2) # round to 2 decimals
        print ("BM5:", temperatureBM5tank, "ºC")
        
        
        # Reading temperature in supply water of the life support system
        tempfileTcap = open("/sys/bus/w1/devices/"+ sondaCap +"/w1_slave")
        thetextTcap = tempfileTcap.read()
        tempfileTcap.close()
        while thetextTcap.split("\n")[0].strip()[-3:] !='YES':
            time.sleep(2)      
            print ("Reading retry of temperature probe in water supply of life support system")
            time.sleep(0.5)
            tempfileTcap = open("/sys/bus/w1/devices/"+ sondaCap +"/w1_slave")
            thetextTcap = tempfileTcap.read()
            tempfileTcap.close()
        tempTcapdata = thetextTcap.split("\n")[1].split(" ")[9]
        temperatureTcap = float(tempTcapdata[2:])
        temperatureTcap = temperatureTcap / 1000
        temperatureTcap = temperatureTcap + calTcap # calibration
        temperatureTcap = round(temperatureTcap, 2) # round to 2 decimals
        print ("Tcap:", temperatureTcap, "ºC")
        
        t=0.5 # waiting time before activating relay modules
        print(" ")
        print("-------------------- Managing relay modules ------------------------------------------")

        time.sleep(t) 
        # conditional for T1         
        if  (float(temperatureT1) < float(set_temp_T1 - histtempT1) and releT1 == 0) or (float(temperatureT1) < float(set_temp_T1 + histtempT1) and releT1 == 1):
            GPIO.output(17, True)
            print(("ReleT1 activated, heating up... --"), ("T1="), (temperatureT1),("<"), ("SET="), (set_temp_T1))
            releT1=1 #reference for the activation of the relay
            time.sleep(t) # heating pulse time
        else:
            GPIO.output(17, False)
            print(("ReleT1 idle"),("T1="),(temperatureT1),(">"), ("SET="), (set_temp_T1))
            releT1=0 #reference of the deactivation of the relay
            time.sleep(t) # waiting time if condition is not met


            # conditional for T2            
        if  (float(temperatureT2) < float(set_temp_T2 - histtempT2) and releT2 == 0) or (float(temperatureT2) < float(set_temp_T2 + histtempT2) and releT2 == 1):
            GPIO.output(18, True)
            print(("ReleT2 activated, heating up... --"), ("T2="), (temperatureT2),("<"), ("SET="), (set_temp_T2))
            releT2=1 #reference for the activation of the relay
            time.sleep(t) # heating pulse time
        else:
            GPIO.output(18, False)
            print(("ReleT2 idle"),("T2="),(temperatureT2),(">"), ("SET="), (set_temp_T2))
            releT2=0 #reference of the deactivation of the relay
            time.sleep(t) # waiting time if condition is not met


            # conditional for T3            
        if  (float(temperatureT3) < float(set_temp_T3 - histtempT3) and releT3 == 0) or (float(temperatureT3) < float(set_temp_T3 + histtempT3) and releT3 == 1):
            GPIO.output(22, True)
            print(("ReleT3 activated, heating up... --"), ("T3="), (temperatureT3),("<"), ("SET="), (set_temp_T3 - histtempT3))
            releT3=1 #reference for the activation of the relay
            time.sleep(t) # heating pulse time
        else:
            GPIO.output(22, False)
            print(("ReleT3 idle"),("T3="),(temperatureT3),(">"), ("SET="), (set_temp_T3))
            releT3=0 #reference of the deactivation of the relay
            time.sleep(t) # waiting time if condition is not met


            # conditional for T4            
        if  (float(temperatureT4) < float(set_temp_T4 - histtempT4) and releT4 == 0) or (float(temperatureT4) < float(set_temp_T4 + histtempT4) and releT4 == 1):
            GPIO.output(23, True)
            print(("ReleT4 activated, heating up... --"), ("T4="), (temperatureT4),("<"), ("SET="), (set_temp_T4))
            releT4=1 #reference for the activation of the relay
            time.sleep(t) # heating pulse time
        else:
            GPIO.output(23, False)
            print(("ReleT4 idle"),("T4="),(temperatureT4),(">"), ("SET="), (set_temp_T4))
            releT4=0 #reference of the deactivation of the relay
            time.sleep(t) # waiting time if condition is not met


            # conditional for T5            
        if  (float(temperatureT5) < float(set_temp_T5 - histtempT5) and releT5 == 0) or (float(temperatureT5) < float(set_temp_T5 + histtempT5) and releT5 == 1):
            GPIO.output(25, True)
            print(("ReleT5 activated, heating up... --"), ("T5="), (temperatureT5),("<"), ("SET="), (set_temp_T5))
            releT5=1 #reference for the activation of the relay
            time.sleep(t) # heating pulse time
        else:
            GPIO.output(25, False)
            print(("ReleT5 idle"),("T5="),(temperatureT5),(">"), ("SET="), (set_temp_T5))
            releT5=0 #reference of the deactivation of the relay
            time.sleep(t) # waiting time if condition is not met


            # conditional for T6            
        if  (float(temperatureT6) < float(set_temp_T6 - histtempT6) and releT6 == 0) or (float(temperatureT6) < float(set_temp_T6 + histtempT6) and releT6 == 1):
            GPIO.output(12, True)
            print(("ReleT6 activated, heating up... --"), ("T6="), (temperatureT6),("<"), ("SET="), (set_temp_T6))
            releT6=1 #reference for the activation of the relay
            time.sleep(t) # heating pulse time
        else:
            GPIO.output(12, False)
            print(("ReleT6 idle"),("T6="),(temperatureT6),(">"), ("SET="), (set_temp_T6))
            releT6=0 #reference of the deactivation of the relay
            time.sleep(t) # waiting time if condition is not met


            # conditional for T7            
        if  (float(temperatureT7) < float(set_temp_T7 - histtempT7) and releT7 == 0) or (float(temperatureT7) < float(set_temp_T7 + histtempT7) and releT7 == 1):
            GPIO.output(16, False)
            print(("ReleT7 activated, heating up... --"), ("T7="), (temperatureT7),("<"), ("SET="), (set_temp_T7))
            releT7=1 #reference for the activation of the relay
            time.sleep(t) # heating pulse time
        else:
            GPIO.output(16, True)
            print(("ReleT7 idle"),("T7="),(temperatureT7),(">"), ("SET="), (set_temp_T7))
            releT7=0 #reference of the deactivation of the relay
            time.sleep(t) # waiting time if condition is not met


            # conditional for T8            
        if  (float(temperatureT8) < float(set_temp_T8 - histtempT8) and releT8 == 0) or (float(temperatureT8) < float(set_temp_T8 + histtempT8) and releT8 == 1):
            GPIO.output(20, False)
            print(("ReleT8 activated, heating up... --"), ("T8="), (temperatureT8),("<"), ("SET="), (set_temp_T8))
            releT8=1 #reference for the activation of the relay
            time.sleep(t) # heating pulse time
        else:
            GPIO.output(20, True)
            print(("ReleT8 idle"),("T8="),(temperatureT8),(">"), ("SET="), (set_temp_T8))
            releT8=0 #reference of the deactivation of the relay
            time.sleep(t) # waiting time if condition is not met


            # conditional for BM1tank            
        if  (float(temperatureBM1tank) < float(set_temp_BM1 - histtempBM1tank) and releBM1tank == 0) or (float(temperatureBM1tank) < float(set_temp_BM1 + histtempBM1tank) and releBM1tank == 1):
            GPIO.output(27, True)
            print(("ReleBM1tank activated, heating up... --"), ("BM1tank="), (temperatureBM1tank),("<"), ("SET="), (set_temp_BM1))
            releBM1tank=1 #reference for the activation of the relay
            time.sleep(t) # heating pulse time
        else:
            GPIO.output(27, False)
            print(("ReleBM1tank idle"),("BM1tank="),(temperatureBM1tank),(">"), ("SET="), (set_temp_BM1))
            releBM1tank=0 #reference of the deactivation of the relay
            time.sleep(t) # waiting time if condition is not met


            # conditional for BM2tank            
        if  (float(temperatureBM2tank) < float(set_temp_BM2 - histtempBM2tank) and releBM2tank == 0) or (float(temperatureBM2tank) < float(set_temp_BM2 + histtempBM2tank) and releBM2tank == 1):
            GPIO.output(24, True)
            print(("ReleBM2tank activated, heating up... --"), ("BM2tank="), (temperatureBM2tank),("<"), ("SET="), (set_temp_BM2))
            releBM2tank=1 #reference for the activation of the relay
            time.sleep(t) # heating pulse time
        else:
            GPIO.output(24, False)
            print(("ReleBM2tank idle"),("BM2tank="),(temperatureBM2tank),(">"), ("SET="), (set_temp_BM2))
            releBM2tank=0 #reference of the deactivation of the relay
            time.sleep(t) # waiting time if condition is not met


            # conditional for BM3tank            
        if  (float(temperatureBM3tank) < float(set_temp_BM3 - histtempBM3tank) and releBM3tank == 0) or (float(temperatureBM3tank) < float(set_temp_BM3 + histtempBM3tank) and releBM3tank == 1):
            GPIO.output(26, False)
            print(("ReleBM3tank activated, heating up... --"), ("BM3tank="), (temperatureBM3tank),("<"), ("SET="), (set_temp_BM3))
            releBM3tank=1 #reference for the activation of the relay
            time.sleep(t) # heating pulse time
        else:
            GPIO.output(26, True)
            print(("ReleBM3tank idle"),("BM3tank="),(temperatureBM3tank),(">"), ("SET="), (set_temp_BM3))
            releBM3tank=0 #reference of the deactivation of the relay
            time.sleep(t) # waiting time if condition is not met


            # conditional for BM4tank            
        if  (float(temperatureBM4tank) < float(set_temp_BM4 - histtempBM4tank) and releBM4tank == 0) or (float(temperatureBM4tank) < float(set_temp_BM4 + histtempBM4tank) and releBM4tank == 1):
            GPIO.output(21, False)
            print(("ReleBM4tank activated, heating up... --"), ("BM4tank="), (temperatureBM4tank),("<"), ("SET="), (set_temp_BM4))
            releBM4tank=1 #reference for the activation of the relay
            time.sleep(t) # heating pulse time
        else:
            GPIO.output(21, True)
            print(("ReleBM4tank idle"),("BM4tank="),(temperatureBM4tank),(">"), ("SET="), (set_temp_BM4))
            releBM4tank=0 #reference of the deactivation of the relay
            time.sleep(t) # waiting time if condition is not met
        
        
        # conditional for BM5tank            
        if  (float(temperatureBM5tank) < float(set_temp_BM5 - histtempBM5tank) and releBM5tank == 0) or (float(temperatureBM5tank) < float(set_temp_BM5 + histtempBM5tank) and releBM5tank == 1):
            GPIO.output(6, False)
            print(("ReleBM5tank activated, heating up... --"), ("BM5tank="), (temperatureBM5tank),("<"), ("SET="), (set_temp_BM5))
            releBM5tank=1 #reference for the activation of the relay
            time.sleep(t) # heating pulse time
        else:
            GPIO.output(6, True)
            print(("ReleBM5tank idle"),("BM5tank="),(temperatureBM5tank),(">"), ("SET="), (set_temp_BM5))
            releBM5tank=0 #reference of the deactivation of the relay
            time.sleep(t) # waiting time if condition is not met
        
        print ("Room temperature: ", temperatureTRoom)
        print ("Temperature of supply water of the aquaria system: ", temperatureTagua)      
        
        Lastdata = time.strftime('%c')
            
        # Send data to text file where they are temporally stored until next reading
        fic = open("/var/www/html/temp/receptor_control.txt", "w")
        data = [str(temperatureT1), str(temperatureT2), str(temperatureT3), str(temperatureT4), str(temperatureT5), str(temperatureT6), str(temperatureT7), str(temperatureT8), str(temperatureBM1tank), str(temperatureBM1blanco), str(temperatureBM1negro), str(temperatureBM2tank), str(temperatureBM2rojo), str(temperatureBM2azul), str(temperatureBM3tank), str(temperatureBM3blanco), str(temperatureBM3negro), str(temperatureBM4tank), str(temperatureBM4rojo), str(temperatureBM4azul),  str(temperatureTRoom), 'ver graficos', str(releT1),  str(releT2),  str(releT3),  str(releT4),  str(releT5),  str(releT6),  str(releT7),  str(releT8),  str(releBM1tank), str(releBM2tank), str(releBM3tank), str(releBM4tank), str(temperatureTagua), str(Lastdata), str(temperatureBM5tank),str(releBM5tank), str(temperatureTcap) ]    

        for line in data:
            fic.write(line)
            fic.write("\n")
        
        fic.close()
        
        print ("Data sent to receptor text file")
        print ("--------------------------------------------------------------")

    # If any of these 2 errors occur, the system will reboot, displaying it on the screen
    except IndexError:
        print ("Rebooting due to IndexError...")
        #os.execv(__file__, sys.argv)
        python = sys.executable
        os.execl(python, python, *sys.argv)
      
    except FileNotFoundError:
        print ("Rebooting due to FileNotFoundError...")
        #os.execv(__file__, sys.argv) 
        python = sys.executable
        os.execl(python, python, *sys.argv)
