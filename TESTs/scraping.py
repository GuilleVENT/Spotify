from bs4 import BeautifulSoup

#import requests

import urllib

import urlparse

import re

import csv

from itertools import izip

#url = raw_input("www.spotontrack.com/playlists/379")

#r = rquests.get("http://"+url)

#data = r.text
url = 'http://www.spotontrack.com/playlists/379'
r = urllib.urlopen('http://www.spotontrack.com/playlists/379').read()

soup = BeautifulSoup(r, "html.parser")

print type(soup)

print("------------------------")

print soup.prettify()

print("------------------------")
print("START")


name = []
link = []
source = r
soup = BeautifulSoup(source, "html.parser")

i = 1 

for li in soup.findAll('a'):
    print li.string
    string = ""
    string = li.string
	#print(link.string,'----------------------', link['href'])
    name.append(string)
	#link.insert(i, link)
	

print "NAME: "
print name

print "NAME 2....................................." 
name2 = []
a = 13
while a < len(name)-7:
    name2.append(name[a])
    a = a + 1

print name2

for lin in soup.find_all('a'):
    link.append(lin.get('href'))

print "LINK ALL ...................................."
print link


print "///////////////////////////////////////////"

spans = soup.find_all('span', {'class' : 'chart-track'})

link_song = []
b = 0
bum = spans[b]
while b < len(spans):
	bum = spans[b]
	for link2 in bum.find_all('a'):
		link_song.append(link2.get('href'))
		b = b + 1


print "SPANS........................................"
print spans 
print "SONG LINKS..................................."
print link_song
print "---------------------------------------------"

name_songs = [span.get_text() for span in spans]
print "SONG NAMES..................................."
print name_songs

print "-----------------------RESULTS------------------------"

count2 = 0 
link_songs2 = []
while count2 <len(link_song):
	temp = link_song[count2]
	temp2 = temp.encode("utf-8")
	link_songs2.append(temp2)
	count2 = count2 + 1

print "SONG LINKS UTF-8..............................."
print link_songs2

count = 0 
name_songs2 = []
while count < len(name_songs):
	temp = name_songs[count]
	temp2 = temp.encode("utf-8")
	name_songs2.append(temp2)
	count = count + 1

print "SONG NAMES UTF-8..............................."
print name_songs2


# SAVING IT IN CSV


with open('PLAYLIST: DEEP FOCUS [379].csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(izip(name_songs2, link_songs2))
