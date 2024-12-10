#Import libraries
from decimal import Decimal
import RPi.GPIO as GPIO
import urllib.request 
import urllib.parse 
import time
import pymysql
import io
import time       
import string     
import re
import os
import sys


try:
    mydb = pymysql.connect(
    host="localhost",
    user= "XXXX", #add info
    passwd="XXXX", #add info
    db="XXX" #add database name
    )

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
    sondaCap = obtain_sonda('Cap')

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
    
    ts=1#  waiting time before retrying to read the probes

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

    # Display data on screen
    print ("T1:", temperatureT1)
    print ("T2:", temperatureT2)
    print ("T3:", temperatureT3)
    print ("T4:", temperatureT4)
    print ("T5:", temperatureT5)
    print ("T6:", temperatureT6)               
    print ("T7:", temperatureT7)
    print ("T8:", temperatureT8)
    print ("BM1tank:", temperatureBM1tank)
    print ("BM1blanco:", temperatureBM1blanco)
    print ("BM1negro:", temperatureBM1negro)
    print ("BM2tank:", temperatureBM2tank)
    print ("BM2rojo:", temperatureBM2rojo)
    print ("BM2azul:", temperatureBM2azul)
    print ("BM3tank:", temperatureBM3tank)
    print ("BM3blanco:", temperatureBM3blanco)
    print ("BM3negro:", temperatureBM3negro)
    print ("BM4tank:", temperatureBM4tank)
    print ("BM4rojo:", temperatureBM4rojo)
    print ("BM4azul:", temperatureBM4azul)
    print ("TRoom:", temperatureTRoom)
    print ("Tagua:", temperatureTagua)
    print ("Tcap:", temperatureTcap)


    # Send data to log database
    data=urllib.parse.urlencode({"T1": temperatureT1, "T2": temperatureT2, "T3": temperatureT3, "T4": temperatureT4, "T5": temperatureT5, "T6": temperatureT6, "T7": temperatureT7, "T8": temperatureT8, "BM1tank": temperatureBM1tank, "BM1blanco": temperatureBM1blanco, "BM1negro": temperatureBM1negro, "BM2tank": temperatureBM2tank, "BM2rojo": temperatureBM2rojo, "BM2azul": temperatureBM2azul, "BM3tank": temperatureBM3tank, "BM3blanco": temperatureBM3blanco, "BM3negro": temperatureBM3negro, "BM4tank": temperatureBM4tank, "BM4rojo": temperatureBM4rojo, "BM4azul": temperatureBM4azul, "TRoom": temperatureTRoom, "Tagua": temperatureTagua, "Tcap": temperatureTcap, "name": "proyect"})
    web=urllib.request.urlopen("http://localhost/temp/log_temp_database.php" + "?" + data)
    print ("Data sent on " + time.strftime('%c') + " to database")  # display if the data have been successfully sent
    web.close()           
     
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
    
    except KeyboardInterrupt:
        pass
