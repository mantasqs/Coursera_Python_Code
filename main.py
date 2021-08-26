import re
import socket
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def MostFreqWord():
    name = input("Enter file name")
    handle = open(name,'r')

    counts = dict()
    for line in handle:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word,0) + 1

    bigCount = None
    bigWord = None
    for word,count in counts.items():
        if bigCount is None or count > bigCount:
            bigWord = word
            bigCount = count

    print(bigWord,bigCount)

def MaxVal(mas):
    biggest = mas[0]
    for nr in mas:
        if nr > biggest:
            biggest = nr
    return biggest

#mas = []
#for i in range(0,4):
#    nr=int(input("Write value"))
#    mas.append(nr)

#print(MaxVal(mas))

def MaxMinValues():
    largest = None
    smallest = None
    while True:
        num = input("Enter a number: ")
        if num == "done":
            break
        try:
            x = int(num)
            if largest is None:
                largest = x
            if smallest is None:
                smallest = x
            
            if x > largest:
                largest = x
            if x < smallest:
                smallest = x
        except:
            print("Invalid input")
    print("Maximum is", largest)
    print("Minimum is", smallest)

def UpperCaseProb():
    fname = input("Enter file name: ")
    fh = open(fname)
    file = fh.read()
    print(file.rstrip().upper())

def prob2():
    # Use the file name mbox-short.txt as the file name
    fname = input("Enter file name: ")
    fh = open(fname)

    count = 0
    s = 0

    for line in fh:
        if line.startswith("X-DSPAM-Confidence:"):
            s += float(line[19:].rstrip())
            count += 1
    print("Average spam confidence:",s/count)

def Prob8_4():
    mas = list()
    fname = input("Enter file name: ")
    fh = open(fname)
    for line in fh:
        for w in line.split():
            if w not in mas:
                mas.append(w)
    mas.sort()
    print(mas)

def Prob8_5():
    fname = input("Enter file name: ")
    if len(fname) < 1:
        fname = "mbox-short.txt"
    fh = open(fname)

    count = 0

    for line in fh:
        if line.startswith("From:"):
            w = line.split()
            print(w[1])
            count += 1
    print("There were",count,"lines in the file with From as the first word")

def Dictionaries():
    purse = dict()
    purse['money'] = 12
    purse['candy'] = 3
    purse['tissues'] = 75
    print(purse)
    print(purse['candy'])
    purse['candy'] = purse['candy'] + 2
    print(purse)

def Dictionaries2():
    counts = dict()
    names = ['csev','cwen','csev','zqian','cwen']
    for name in names:
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] = counts[name] + 1
    print(counts)

def Dictionaries2Quicker():
    counts = dict()
    names = ['csev','cwen','csev','zqian','cwen']
    for name in names:
        counts[name] = counts.get(name,0) + 1
    print(counts)

def Dictionaries3():
    counts = dict()
    print("Enter a line of text:")
    line =  input('')

    words = line.split()

    print("Words:", words)

    print("Counting...")
    for word in words:
        counts[word] = counts.get(word,0) + 1
    print('Counts',counts)

def Prob9_4():
    fname = input("Enter file name: ")
    fhandler = open(fname)

    words = list()
    counts = dict() 
    for line in fhandler:
        if line.startswith("From:"):
            words = line.split()
            counts[words[1]] = counts.get(words[1],0) + 1
    
    biggestCount = None
    biggestWord = None
    for word,count in counts.items():
        if biggestCount is None or biggestCount < count:
            biggestCount = count
            biggestWord = word
    print(biggestWord,biggestCount)

def Tuples():
    x = ('Glenn','Sally','Joseph')
    (x1,y) = (4,'fred')
    print(y)

#Reverse Tuple (Shoter version)
    c = {'a':10,'b':1,'c':22}
    print(sorted([(v,k)for k,v in c.items()]))

#Reverse Tuple (Longer version)
    lst = list()
    for key, val in c.items():
        newtup = (val, key)
        lst.append(newtup)
    print(sorted(lst))

def Prob10_2():
    lst = list()
    count = dict()
    fname = input("Enter file name:")
    if len(fname)<1:
        fname = "mbox-short.txt"
    fhandle = open(fname)
    for line in fhandle:
        if line.startswith("From "):
            pos = line.find(":")
            count[line[pos-2:pos]]=count.get(line[pos-2:pos],0) + 1
    for k,v in count.items():
        lst.append((k,v))
    lst = sorted(lst)
    for k,v in lst:
        print(k,v)

#REGULAR EXPRESIONS COURSE 3 WEEK 2
def ExtractSumOfNumbersInAFile():
    fname = input("Enter file name:")
    fh = open(fname)
    file = fh.read()
    suma = 0
    y = re.findall('[0-9]+',file)
    for num in y:
        suma +=int(num) 
    print(suma)

#SOCKETS COURSE 3 WEEK 3
def SocketIntro():
    mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print(data.decode())
    mysock.close()

def Socket2():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()

#COURSE 3 WEEK 4 urllib (OPEN WEBPAGE CONTENT)
def UrllibFunc():
    fileHandndler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    for line in fileHandndler:
        print(line.decode().strip())
UrllibFunc()

def CountWordsInWebPage():
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    counts = dict()
    countWords = 0
    for line in fhand:
        words = line.decode().split()
        for word in words:
            counts[word] = counts.get(word,0) + 1
            countWords += 1
    print(counts)
    print("\nThere are",countWords,"words in this webpage.")

def BeautifulSoupFunc():
    url = input('Enter - ')
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        print(tag.get('href',None))

import ssl
#Ignore SSL CERTIFICATE ERRORS
def SSL():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

def Prob_Scraping_HTML_Data_with_BeautifulSoup():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = "http://py4e-data.dr-chuck.net/comments_1299240.html"
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    suma = 0
    count = 0
    # Retrieve td tags
    tags = soup('span')
    for tag in tags:
        suma += int(tag.contents[0])
        count += 1
    print("Count",count)
    print("Sum",suma)

def Assignment_Following_Links_in_HTML_Using_BeautifulSoup():
    url = "http://py4e-data.dr-chuck.net/known_by_Tembe.html"
    count = int(input("Enter count:"))
    position = int(input("Enter position:"))
    print("Retrieving:",url)

    for i in range(0,count):
        index = 1
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')

        for tag in tags:
            if index == position:
                url = tag.get('href',None)
                print("Retrieving:",url)
                break
            index = index + 1

import xml.etree.ElementTree as ET

def Web_ServicesXML():
    data = '''
    <person>
        <name>Chuck</name>
        <phone type="intl">
            +1 734 303 4456
        </phone>
        <email hide="yes"/>
    </person>
    '''
    tree = ET.fromstring(data)
    print('Name:',tree.find('name').text)
    print('Attr:',tree.find('email').get('hide'),"\n")

    # multiple nodes
    input = '''
    <stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>Brent</name>
            </user>
        </users>
    </stuff>
    '''
    stuff = ET.fromstring(input)
    lst = stuff.findall('users/user')
    print('User count:', len(lst),"\n")
    for item in lst:
        print('Name',item.find('name').text)
        print('Id',item.find('id').text)
        print('Attribute', item.get("x"))

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

def Assignment_Extracting_Data_from_XML():

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    
    url = "http://py4e-data.dr-chuck.net/comments_1299242.xml"

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)

    suma = 0
    data = uh.read()
    #print('Retrieved', len(data), 'characters')
    #print(data.decode())
    tree = ET.fromstring(data)
    counts = tree.findall('comments/comment')
    for item in counts:
        suma += int(item.find('count').text)
    print("sum:",suma)


#COURSE 3 WEEK 6 (JSON)
import json
def JSON_Intro():
    data = '''
    {
        "name" : "Chuck",
        "phone" : {
            "type" : "intl",
            "number" : "+1 734 303 4456"
        },
        "email" : {
            "hide" : "yes"
        }
    }
    '''
    info = json.loads(data)
    print('Name:',info["name"])
    print('Hide:',info["email"]["hide"])
    print(info["phone"]["type"],info["phone"]["number"])

import urllib.request, urllib.parse, urllib.error
import json
def GoogleAPI():
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

    while True:
        address = input('Enter location: ')
        if len(address) < 1: break

        url = serviceurl + urllib.parse.urlencode({'address': address})

        print('Retrieving', url)
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')

        try:
            js = json.laods(data)
        except:
            js = None
        
        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            print(data)
            continue
        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js["results"][0]["geometry"]["location"]["lng"]
        print('lat', lat, 'lng', lng)
        location = js ['results'][0]['formatted_address']
        print(location)

def Assignment_Extracting_Data_from_JSON():
    url = "http://py4e-data.dr-chuck.net/comments_1299243.json"
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    info = json.loads(data)
    sum_of_count = 0
    count = 0
    for item in info['comments']:
        sum_of_count += int(item['count'])
        count += 1
    print("Count:",count)
    print("Sum:",sum_of_count)


import urllib.request, urllib.parse, urllib.error
import json
import ssl

def Assignment_Using_the_GeoJSON_API():
    api_key = False
    # If you have a Google Places API key, enter it here
    # api_key = 'AIzaSy___IDByT70'
    # https://developers.google.com/maps/documentation/geocoding/intro

    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    else :
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        address = "Technical University of Cluj-Napoca"
        if len(address) < 1:break

        params = dict()
        params['address'] = address
        if api_key is not False: params['key'] = api_key
        url = serviceurl + urllib.parse.urlencode(params)

        print("Retrieving", url)
        
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
        
        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            print(data)
            continue
        id = js["results"][0]["place_id"]
        print(id)
        break

def PeerGrade_FindMaxVal():
    lst = [15,16,20,4,6,8,-1,5,-3]
    biggest = None
    for nr in lst:
        if biggest is None:
            biggest = nr
        if nr > biggest:
            biggest = nr
    print("Biggest number in list is:",biggest)

#COURSE 4 WEEK 1 (CLASSES)
def classes():
    class PartyAnimal:
        x=0
        name = ""

        def __init__(self,z):
            self.name = z
            print("I am constructor")

        def party(self):
            self.x = self.x + 1
            print(self.name,": So far",self.x)
        
        def __del__(self):
            print("I am destructor")

    an = PartyAnimal("Sally")

    an.party()
    an.party()
    an.party()

    #Inheritance
    class FootballFan(PartyAnimal):
        points = 0
        def touchdown(self):
            self.points = self.points + 7
            self.party()
            print(self.name,": points", self.points)
    j = FootballFan("Jim")
    j.party()
    j.touchdown()

#COURSE 4 WEEK 2 (SQLITE)
import sqlite3

def Assignment_Counting_Email_in_a_Database():
    conn = sqlite3.connect('emaildb.sqlite')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Counts')

    cur.execute('''
    CREATE TABLE Counts (org TEXT, count INTEGER)''')

    fname = input('Enter file name: ')
    if (len(fname) < 1): fname = 'mbox.txt'
    fh = open(fname)

    for line in fh:
        if not line.startswith('From: '): continue
        pieces = line.split()
        email = pieces[1]
        org = email.split("@")[1]
        #org = re.findall("@(.+)",email)[0]
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (org,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                        (org,))
        conn.commit()

    # https://www.sqlite.org/lang_select.html
    sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

    for row in cur.execute(sqlstr):
        print(str(row[0]), row[1])

    cur.close()




def Assignment_Musical_Track_Database():

    import xml.etree.ElementTree as ET
    import sqlite3

    conn = sqlite3.connect('trackdb.sqlite')
    cur = conn.cursor()

    # Make some fresh tables using executescript()
    cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;
    DROP TABLE IF EXISTS Genre;

    CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE
    );

    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY 
            AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    );
    ''')


    fname = input('Enter file name: ')
    if ( len(fname) < 1 ) : fname = 'Library.xml'

    # <key>Track ID</key><integer>369</integer>
    # <key>Name</key><string>Another One Bites The Dust</string>
    # <key>Artist</key><string>Queen</string>

    def lookup(d, key):
        found = False
        for child in d:
            if found : return child.text
            if child.tag == 'key' and child.text == key :
                found = True
        return None

    stuff = ET.parse(fname)
    all = stuff.findall('dict/dict/dict')
    print('Dict count:', len(all))
    for entry in all:
        if ( lookup(entry, 'Track ID') is None ) : continue

        name = lookup(entry, 'Name')
        artist = lookup(entry, 'Artist')
        album = lookup(entry, 'Album')
        genre = lookup(entry,'Genre')
        count = lookup(entry, 'Play Count')
        rating = lookup(entry, 'Rating')
        length = lookup(entry, 'Total Time')

        if name is None or artist is None or album is None or genre is None: 
            continue

        print(artist, artist, album, genre)

        cur.execute('''INSERT OR IGNORE INTO Artist (name) 
            VALUES ( ? )''', ( artist, ) )
        cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
        artist_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Genre (name)
            VALUES ( ? )''',(genre, ) )
        cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
        genre_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
            VALUES ( ?, ? )''', ( album, artist_id ) )
        cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
        album_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Track
            (Title, Album_id, Genre_id, Len, Rating, Count) 
            VALUES ( ?, ?, ?, ?, ?, ? )''', 
            ( name, album_id, genre_id, length, rating, count))

        conn.commit()

def Assignment_Many_Students_in_Many_Courses():
    import json
    import sqlite3

    conn = sqlite3.connect('rosterdb.sqlite')
    cur = conn.cursor()

    # Do some setup
    cur.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Member;
    DROP TABLE IF EXISTS Course;

    CREATE TABLE User (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name   TEXT UNIQUE
    );

    CREATE TABLE Course (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title  TEXT UNIQUE
    );

    CREATE TABLE Member (
        user_id     INTEGER,
        course_id   INTEGER,
        role        INTEGER,
        PRIMARY KEY (user_id, course_id)
    )
    ''')

    fname = input('Enter file name: ')
    if len(fname) < 1:
        fname = 'roster_data_sample.json'

    # [
    #   [ "Charley", "si110", 1 ],
    #   [ "Mea", "si110", 0 ],

    str_data = open(fname).read()
    json_data = json.loads(str_data)

    for entry in json_data:

        name = entry[0]
        title = entry[1]
        role = entry[2]

        print((name, title, role))

        cur.execute('''INSERT OR IGNORE INTO User (name)
            VALUES ( ? )''', ( name, ) )
        cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
        user_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Course (title)
            VALUES ( ? )''', ( title, ) )
        cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
        course_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Member
            (user_id, course_id, role) VALUES ( ?, ?, ? )''',
            ( user_id, course_id, role ) )

        conn.commit()