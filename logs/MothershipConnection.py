from bs4 import BeautifulSoup

#import requests

import urllib

import urlparse

import re

import csv

from itertools import izip

import requests

import json



#######################################################
########## TO FIRE SNOOPY WITHOUT MOTHERSHIP ##########

'''GIVE SPOTONTRACK PLAYLIST URL'''
#######################################################
url = 'http://www.spotontrack.com/playlists/379'
#######################################################


'''GIVE NAME TO THE OUTPUT CSV FILE'''
#######################################################
name_csv = 'PLAYLIST: DEEP FOCUS [379].csv'
#######################################################

########## TO FIRE SNOOPY WITHOUT MOTHERSHIP ##########
#######################################################


'''DO YOU WANNA DOWNLOAD THE 30s SNIPPLET?'''
DOWNLOAD = "TRUE"


def Snoopy(url , name_csv):
    r = urllib.urlopen(url).read()

    soup = BeautifulSoup(r, "html.parser")

 #print type(soup)

 #print("------------------------")

 #print soup.prettify()

 #print("------------------------")
 #print("START")


    name = []
    link = []
    source = r
    soup = BeautifulSoup(source, "html.parser")

    i = 1 

    for li in soup.findAll('a'):
     #print li.string
        string = ""
        string = li.string
	 #print(link.string,'----------------------', link['href'])
        name.append(string)
	 #link.insert(i, link)
	

 #print "NAME: "
 #print name

 #print "NAME 2....................................." 
    name2 = []
    a = 13
    while a < len(name)-7:
        name2.append(name[a])
        a = a + 1

 #print name2

    for lin in soup.find_all('a'):
        link.append(lin.get('href'))

 #print "LINK ALL ...................................."
 #print link


 #print "///////////////////////////////////////////"

    spans = soup.find_all('span', {'class' : 'chart-track'})

    link_song = []
    b = 0
    bum = spans[b]
    while b < len(spans):
        bum = spans[b]
        for link2 in bum.find_all('a'):
		    link_song.append(link2.get('href'))
		    b = b + 1


    #print "SPANS........................................"
    #print spans 
    #print "SONG LINKS..................................."
    #print link_song
    #print "---------------------------------------------"

    name_songs = [span.get_text() for span in spans]
    #print "SONG NAMES..................................."
    #print name_songs

    print "-----------------------RESULTS------------------------"

    count2 = 0 
    link_songs2 = []
    while count2 <len(link_song):
	    temp = link_song[count2]
	    temp2 = temp.encode("utf-8")
	    link_songs2.append(temp2)
	    count2 = count2 + 1

#print "SONG LINKS UTF-8..............................."
#print link_songs2

    count = 0 
    name_songs2 = []
    while count < len(name_songs):
        temp = name_songs[count]
        temp2 = temp.encode("utf-8")
        name_songs2.append(temp2)
        count = count + 1

#print "SONG NAMES UTF-8..............................."
#print name_songs2

    number_list = []
    link_song_spotify_temp = []
    link_song_spotify_def  = []
    id_list = []
    name_artist = []
    name_artist_def =[] 
    name_artist_utf8 = []
    body = []
    bodies = []

    preview_url = []
    preview_url_def = []
    
    H = 0


    while H < len(link_songs2):
        ulrsong   =   link_songs2[H]
        oona    =   urllib.urlopen(ulrsong).read()
        soupsong  =   BeautifulSoup(oona, "html.parser")
        '''
        ######## ARTIST NAME ########
        name[H] = soupsong.title.string
        name_artist = name[H]
        guion_count = name_artist.count('-')

        if guion_count == 2:
    	    guion = name_artist.index('-')
    	    name_artist_def.append(name_artist[guion:])
        else:
            guion = name_artist.index('-')
    	    temp6 = name_artist[guion:]
    	    guion2 = temp6.index('-')
    	    name_artist_def.append(temp6[guion2:])

        temp7 = name_artist_def[H]
        temp8 = temp7[:-17]
        name_artist_def[H] = temp8[2:]
        name_artist_ = name_artist_def[H]
        name_artist_utf8.append(name_artist_.encode("utf-8"))
        print name_artist_def[H]
        '''
        ######## PLAYLIST POSITION ########
        number_list.append(H+1) 

        ######## LINKS and ID's ########
        conect = soupsong.find('a', {'target' : '_blank' , 'class' : 'btn-u btn-block btn-u margin-bottom-10'})

        link_song_spotify_temp.append(conect.get('href'))
        value = link_song_spotify_temp[H]
        link_song_spotify_def.append(value.encode("utf-8"))
        id_list.append(value[31:])
        #print id_list[H]
        #print link_song_spotify_temp[H]

        ######## 30s PREVIEW URL ########
        id_temp = id_list[H]
        #print id_temp
        id_temp_str = str(id_temp)
        id_list[H] = id_list[H].encode("utf-8")
        urlid = 'https://api.spotify.com/v1/tracks/' + id_temp_str
        headers = {'id':id_temp_str, 'cache-control':"no-cache", 'postman-token':"2bf1de22-4252-d879-e988-6223d70b8e75"}
        response = requests.request("GET", urlid, headers=headers)
        data = json.loads(response.text)
        #print data
        album_song = data['album']
        artist = album_song['artists']
        
        #print album_song
        #print artist
        artist_name = artist[0]
        artist_name_ = artist_name['name']
        print artist_name_
        artist_name_ = artist_name_.encode("utf-8")
        #print id_temp
        name_artist_def.append(artist_name_)
        preview_url.append(data['preview_url'])
        print id_list[H]
        print link_song_spotify_temp[H]
        print(preview_url[H])
        if preview_url[H] != None:
            preview_url[H] = preview_url[H].encode("utf-8")
            if DOWNLOAD == "TRUE":
                
                name_mp3 = "Song: " + artist_name_ + id_temp_str + ".mp3"
                urllib.urlretrieve (preview_url[H], name_mp3)
                print "Song Downloaded"
    
        H = H + 1
    



 #print(preview_url)

 # SAVING IT IN CSV
    with open(name_csv, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(izip(number_list, name_songs2, name_artist_def, link_songs2, link_song_spotify_def, id_list, preview_url))

#TO FIRE SNOOPY WITHOUT MOTHERSHIP.py
Snoopy(url, name_csv)


