from bs4 import BeautifulSoup

#import requests

import urllib

import urlparse

import re

import csv

from itertools import izip

import requests

import json

import MothershipConnection

from datetime import datetime 

import sched, time

url = 'http://www.spotontrack.com/playlists/379'
name_csv = 'PLAYLIST: DEEP FOCUS [379].csv'

url_list = ['http://www.spotontrack.com/playlists/379','http://www.spotontrack.com/playlists/379','http://www.spotontrack.com/playlists/379','http://www.spotontrack.com/playlists/379','http://www.spotontrack.com/playlists/379','http://www.spotontrack.com/playlists/379']
name_list = ['DEEP FOCUS [379]','DEEP FOCUS [379]','DEEP FOCUS [379]','DEEP FOCUS [379]','DEEP FOCUS [379]','DEEP FOCUS [379]']
csv_list_name = ['TIME:','TIME:','TIME:','TIME:','TIME:','TIME:','TIME:','TIME:','TIME:']
date_format = '%d-%m-%Y-%M-%H_{fname}'


#HAVE A MEGA FUNCTION HERE THAT ACTIVATES THE MOTHERSHIP WHEN A SPECIFIC TIME IS 
#WE WILL CALL IT MOTHER
#THEN MOTHER THE ACTIVATION CODE AND SETS THE MOTHERSHIP FREE
# ==== MOTHER CALLS THE CODE DOWN HERE 
ON = "TRUE"



def MOTHER( ON ):
    while ON == "TRUE":
        print "MOTHER AWAKED....................."
        print "ACTIVATING MOTHERSHIP............."
        MothershipACTIVATION()
        print "COMPLETION........................"
        timenow = datetime.now()
        timenow_ = str(timenow)
        timenow__ = timenow_[10:]
        timenow___ = timenow__[:-7]
        print "Mother is sleeping untill tomorrow at :"+ timenow___  
        time.sleep(86400)





def MothershipACTIVATION():
    i=0
    while i < len(url_list):
        linklist = url_list[i] 
        linklist_ = str(linklist)
        idlist = linklist_[37:]



        timenow = datetime.now()
        temp00 = str(timenow)
        temp01 = temp00[:-7]
        temp11 = csv_list_name[i]
	    #temp22 = name_list[i]
        temp33 = ""
        temp12 = str(temp11)
	    #temp23 = str(temp22)
        temp33 = "ID: " + idlist + " TIME: " + temp01
        temp34 = str(temp33)
        csv_list_name[i] = temp34
        #print(csv_list_name[i])

        # conseguido ! ahora he visto que el nombre de la playlist es una idiotez tenerlo, mucho trabajo manual, porahora innecesarion mas adelante se puede hacer ! pero por ahora lo voy a dejar fuera
        print "MOTHERSHIP CONNECTING............."
        print "Creating FILE : " + csv_list_name[i]
        MothershipConnection.Snoopy(url_list[i], csv_list_name[i])
        i=i+1




if ON == "TRUE":
    MOTHER(ON)






#MothershipConnection.Snoopy(url_list[i], csv_list_name[i])