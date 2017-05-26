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

#url = 'http://www.spotontrack.com/playlists/379'
#name_csv = 'PLAYLIST: DEEP FOCUS [379].csv'

''' THIS IS A LIST OF URLs OF ALL THE PLAYLISTS IN SPOTIFY THAT HAVE MORE THAN A MILL FOLLOWERS'''
url_list = ['http://www.spotontrack.com/playlists/879549','http://www.spotontrack.com/playlists/379','http://www.spotontrack.com/playlists/68874','http://www.spotontrack.com/playlists/127201','http://www.spotontrack.com/playlists/879552','http://www.spotontrack.com/playlists/511794','http://www.spotontrack.com/playlists/247834','http://www.spotontrack.com/playlists/868254','http://www.spotontrack.com/playlists/868253','http://www.spotontrack.com/playlists/868252','http://www.spotontrack.com/playlists/190328','http://www.spotontrack.com/playlists/679633','http://www.spotontrack.com/playlists/868256','http://www.spotontrack.com/playlists/760517','http://www.spotontrack.com/playlists/760513','http://www.spotontrack.com/playlists/738910','http://www.spotontrack.com/playlists/738909','http://www.spotontrack.com/playlists/738926','http://www.spotontrack.com/playlists/738905','http://www.spotontrack.com/playlists/141449','http://www.spotontrack.com/playlists/760515','http://www.spotontrack.com/playlists/738907','http://www.spotontrack.com/playlists/760518','http://www.spotontrack.com/playlists/497587','http://www.spotontrack.com/playlists/231122','http://www.spotontrack.com/playlists/72762','http://www.spotontrack.com/playlists/748174','http://www.spotontrack.com/playlists/748177','http://www.spotontrack.com/playlists/748326','http://www.spotontrack.com/playlists/738908','http://www.spotontrack.com/playlists/23108','http://www.spotontrack.com/playlists/728392','http://www.spotontrack.com/playlists/76755','http://www.spotontrack.com/playlists/738906','http://www.spotontrack.com/playlists/597046','http://www.spotontrack.com/playlists/728397','http://www.spotontrack.com/playlists/717760','http://www.spotontrack.com/playlists/235613','http://www.spotontrack.com/playlists/235620','http://www.spotontrack.com/playlists/717402','http://www.spotontrack.com/playlists/242029','http://www.spotontrack.com/playlists/204429','http://www.spotontrack.com/playlists/717394','http://www.spotontrack.com/playlists/185360','http://www.spotontrack.com/playlists/728393','http://www.spotontrack.com/playlists/190281','http://www.spotontrack.com/playlists/187383','http://www.spotontrack.com/playlists/717398','http://www.spotontrack.com/playlists/717397','http://www.spotontrack.com/playlists/717401','http://www.spotontrack.com/playlists/190317','http://www.spotontrack.com/playlists/728396','http://www.spotontrack.com/playlists/4004','http://www.spotontrack.com/playlists/707981','http://www.spotontrack.com/playlists/707977','http://www.spotontrack.com/playlists/707972','http://www.spotontrack.com/playlists/4002','http://www.spotontrack.com/playlists/511843','http://www.spotontrack.com/playlists/690203','http://www.spotontrack.com/playlists/690206','http://www.spotontrack.com/playlists/690197','http://www.spotontrack.com/playlists/502365','http://www.spotontrack.com/playlists/690201','http://www.spotontrack.com/playlists/690204','http://www.spotontrack.com/playlists/690200','http://www.spotontrack.com/playlists/30107','http://www.spotontrack.com/playlists/690199','http://www.spotontrack.com/playlists/285801','http://www.spotontrack.com/playlists/689659','http://www.spotontrack.com/playlists/596637','http://www.spotontrack.com/playlists/290549','http://www.spotontrack.com/playlists/689660','http://www.spotontrack.com/playlists/666861','http://www.spotontrack.com/playlists/690205','http://www.spotontrack.com/playlists/190290','http://www.spotontrack.com/playlists/690202','http://www.spotontrack.com/playlists/666862','http://www.spotontrack.com/playlists/84047','http://www.spotontrack.com/playlists/22202','http://www.spotontrack.com/playlists/666857','http://www.spotontrack.com/playlists/632118','http://www.spotontrack.com/playlists/649114','http://www.spotontrack.com/playlists/659315','http://www.spotontrack.com/playlists/666866','http://www.spotontrack.com/playlists/290510','http://www.spotontrack.com/playlists/666865','http://www.spotontrack.com/playlists/659308','http://www.spotontrack.com/playlists/124770','http://www.spotontrack.com/playlists/659317','http://www.spotontrack.com/playlists/659316','http://www.spotontrack.com/playlists/641349','http://www.spotontrack.com/playlists/649140','http://www.spotontrack.com/playlists/290515','http://www.spotontrack.com/playlists/190347','http://www.spotontrack.com/playlists/641365','http://www.spotontrack.com/playlists/190271','http://www.spotontrack.com/playlists/641357','http://www.spotontrack.com/playlists/641363'] 
#name_list = ['DEEP FOCUS [379]','DEEP FOCUS [379]','DEEP FOCUS [379]','DEEP FOCUS [379]','DEEP FOCUS [379]','DEEP FOCUS [379]']
csv_list_name = []



#HAVE A MEGA FUNCTION HERE THAT ACTIVATES THE MOTHERSHIP WHEN A SPECIFIC TIME IS 
#WE WILL CALL IT MOTHER
#THEN MOTHER THE ACTIVATION CODE AND SETS THE MOTHERSHIP FREE
# ==== MOTHER CALLS THE CODE DOWN HERE 

###################### TURN MOTHER ON ######################
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
        #temp11 = csv_list_name[i]
	    #temp22 = name_list[i]
        temp33 = ""
        #temp12 = str(temp11)
	    #temp23 = str(temp22)
        temp33 = "ID: " + idlist + " TIME: " + temp01 + ".csv"
        temp34 = str(temp33)
        csv_list_name.append(temp34)
        #print(csv_list_name[i])

        # conseguido ! ahora he visto que el nombre de la playlist es una idiotez tenerlo, mucho trabajo manual, porahora innecesarion mas adelante se puede hacer ! pero por ahora lo voy a dejar fuera
        print "MOTHERSHIP CONNECTING............."
        print "Creating FILE : " + csv_list_name[i]
        MothershipConnection.Snoopy(url_list[i], csv_list_name[i])
        i=i+1




if ON == "TRUE":
    MOTHER(ON)
