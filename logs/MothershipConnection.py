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
#url = 'http://www.spotontrack.com/playlists/379'
#######################################################


'''GIVE NAME TO THE OUTPUT CSV FILE'''
#######################################################
#name_csv = 'PLAYLIST: DEEP FOCUS [379].csv'
#######################################################

########## TO FIRE SNOOPY WITHOUT MOTHERSHIP ##########
#######################################################


'''DO YOU WANNA DOWNLOAD THE 30s SNIPPLET?'''
DOWNLOAD = "FALSE"
'''DO YOU WANNA GET AUDIO FEATURES THROU SPOTIFY API '''
get_features = "FALSE"


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
    link_songs2 = ["LINK SPOTON"]
    while count2 <len(link_song):
	       temp = link_song[count2]
	       temp2 = temp.encode("utf-8")
	       link_songs2.append(temp2)
	       count2 = count2 + 1

#print "SONG LINKS UTF-8..............................."
#print link_songs2

    count = 0 
    name_songs2 = ["Song"]
    while count < len(name_songs):
        temp = name_songs[count]
        temp2 = temp.encode("utf-8")
        name_songs2.append(temp2)
        count = count + 1

#print "SONG NAMES UTF-8..............................."
#print name_songs2

    number_list = ["Pos."]
    link_song_spotify_temp = []
    link_song_spotify_def  = ["LINK SPOTIFY"]
    id_list = ["ID"]
    name_artist = []
    name_artist_def =["Artist"] 
    name_artist_utf8 = []
    body = []
    bodies = []

    preview_url = ["30s-Preview"]
    preview_url_def = []

    # IF FEATURES FROM SPOTONTRACK
    feat_BPM   = ["BPM"]
    feat_KEY   = ["KEY"]
    feat_Mode  = ["MODE"]
    feat_Dance = ["DANCEABILITY"]
    feat_Valence= ["VALENCE"]
    feat_Energy = ["ENERGY"]
    feat_Acousticness = ["ACOUSTICNESS"]
    feat_Instrumentalness = ["INSTRUMENTALNESS"]
    feat_Liveness = ["LIVENESS"]
    feat_Speechiness = ["SPEECHINESS"]

   # IF FEATURES FROM SPOTIFY API
    danceability = []
    energy  = []
    key  = []
    loudness = []
    mode = []
    speechiness = []
    acousticness = []
    instrumentalness = []
    liveness = []
    valence = []
    tempo = []
    duration_ms = []
    time_signature = []
    

    H = 0
    G = 1

    while H < len(link_songs2)+1: #len(link_songs2)'''
        
        ulrsong   =   link_songs2[G]
        
        oona    =   urllib.urlopen(ulrsong).read()
        soupsong  =   BeautifulSoup(oona, "html.parser")

        feat = soupsong.find('div', {'class':'col-md-3'})
        #print feat
        #print "-----"
        try:
            feat2 = feat.find_all('div')[4].text.split('\n')
            #print feat2
            feat_BPM.append(feat2[1][4:])
            feat_KEY.append(feat2[4][27:])
            feat_Mode.append(feat2[7][58:])
            feat_Dance.append(feat2[9][13:])
            feat_Valence.append(feat2[11][8:])
            feat_Energy.append(feat2[13][7:])
            feat_Acousticness.append(feat2[15][13:])
            feat_Instrumentalness.append(feat2[17][17:])
            feat_Liveness.append(feat2[19][9:])
            feat_Speechiness.append(feat2[21][12:])
        except IndexError:
            #in this case call spotify api would not happen very often 
            feat_BPM.append("None")
            feat_KEY.append("None")
            feat_Mode.append("None")
            feat_Dance.append("None")
            feat_Valence.append("None")
            feat_Energy.append("None")
            feat_Acousticness.append("None")
            feat_Instrumentalness.append("None")
            feat_Liveness.append("None")
            feat_Speechiness.append("None")
        '''
        print "+++++"
        print feat_BPM[G]
        print feat_KEY[G]   #sehr komisch aber whatever ist nicht wichtig
        print feat_Mode[G] #hier auch, whatever ! solutionated 
        print feat_Dance[G]
        print feat_Valence[G]         # WENN ICH NUR DIE ZAHL HABEN WILL MUSS ICH NUR DEN STRING SCHNEIDEN 
        print feat_Energy[G]
        print feat_Acousticness[G]
        print feat_Instrumentalness[G]
        print feat_Liveness[G]
        print feat_Speechiness[G]
        '''

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
        id_temp = id_list[G]
        #print id_temp
        id_temp_str = str(id_temp)
        id_list[G] = id_list[G].encode("utf-8")
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
        print id_list[G]
        print link_song_spotify_temp[H]
        print(preview_url[G])
        # FEATURES THROUGH SPOTIFY API.
        '''
        if get_features == "TRUE":
            url_features = "https://api.spotify.com/v1/audio-features/" + id_temp_str
            headers2 = {'accept': "application/json",'authorization': "Bearer BQDHlGRGG7cbUFZZzMegp2kVeh5RwM0ODJSW8gImmOvuxu2rCYTGgTWpav8HthqYegIuKtfBPlkLtU77I2y8Ew81q9hxSoCmgeQiD11SuBzRmPcCMQiTmMH4TF9-az63sa0WdDbBcNwt7yOPvFRshj413l51j6Yt-4EdE7J6gpbDLHlSDvBm-YcF16TU3AkP2cTAkzQUc4ooz7ErVtueJJ-Ac_m3v5fP3X1U0syGjz4cYQRndEfUPF9wZsVmjnFL7t26DV5ZfNBE-zhILm3uRLsGKFb4jgJFe_MWPzcl2RKVdKee2PXZvM4KA_hg7VPqaNwXmEPDXqn4"}
            response2 = requests.request("GET", url_features, headers=headers2)
            features = json.loads(response2.text)

            danceability.append(features['danceability'])
            energy.append(features['energy'])
            key.append(features['key'])
            loudness.append(features['loudness'])
            mode.append(features['mode'])
            speechiness.append(features['speechiness'])
            acousticness.append(features['acousticness'])
            instrumentalness.append(features['instrumentalness'])
            liveness.append(features['liveness']) 
            valence.append(features['valence'])        
            tempo.append(features['tempo'])        
            duration_ms.append(features['duration_ms'])
            time_signature.append(features['time_signature'])
        '''
        if preview_url[G] != None:
            preview_url[G] = preview_url[G].encode("utf-8")
            if DOWNLOAD == "TRUE":
                slash = artist_name_.count('/')
                if slash == 0:  #TO GET OVER THAT BUG JUST FOR NOW ARTIST NAME AU/RA FUCKS IT ALL UP
                    name_mp3 = "Song: " + str(artist_name_) + " " + id_temp_str + ".mp3"
                    urllib.urlretrieve (preview_url[G], name_mp3)
                    print "Song Downloaded"
        G = G + 1
        if G == len(link_songs2):
            break 
        else:
            H = H+1
    

    

 #print(preview_url)

 # SAVING IT IN CSV
    with open(name_csv, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(izip(number_list, name_songs2, name_artist_def, link_songs2, link_song_spotify_def, id_list, preview_url, feat_BPM,feat_KEY ,feat_Mode,feat_Dance,feat_Energy,feat_Valence,feat_Acousticness,feat_Instrumentalness,feat_Speechiness,feat_Liveness))

#TO FIRE SNOOPY WITHOUT MOTHERSHIP.py
#Snoopy(url, name_csv)


