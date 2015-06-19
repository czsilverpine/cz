import sgmllib,re

class MyTracks(sgmllib.SGMLParser):
    "A simple parser class."
    def parse(self, s):
        "Parse the given string 's'."
        self.feed(s)
        self.close()

    def __init__(self, verbose=0):
        "Initialise an object, passing 'verbose' to the superclass."
        sgmllib.SGMLParser.__init__(self, verbose)
        self.hyperlinks = []
        self.musictime = []
        self.name = []
        self.m = 0
        self.is_a = 0

    def start_a(self, attributes):
        "Process a hyperlink and its 'attributes'."
        for name, value in attributes:
            if name == "href" and re.findall(r'\A/music/.+/_/',value):
                  self.is_a=1
                  if self.m==0 or value!=self.hyperlinks[self.m-1]:
                     self.hyperlinks.append(value)
                     self.m=self.m+1
                 
    def get_hyperlinks(self):
        "Return the list of hyperlinks."
        return self.hyperlinks

    def end_a(self):   
        self.is_a=0 

    def handle_data(self, text):   
        if self.is_a:   
                self.name.append(text)   

    def start_abbr(self, attributes):
        for name, value in attributes:
            if name == "title":
                  self.musictime.append(value)

    def get_musictime(self):
        "Return the list of musictime."
        return self.musictime 


import sgmllib,re

class MyFriends(sgmllib.SGMLParser):
    "A simple parser class."
    is_a=""   
 
    def parse(self, s):
        "Parse the given string 's'."
        self.feed(s)
        self.close()

    def __init__(self, verbose=0):
        "Initialise an object, passing 'verbose' to the superclass."
        sgmllib.SGMLParser.__init__(self, verbose)
        self.hyperlinks = []
        self.name=[]

    def start_a(self, attributes):
        "Process a hyperlink and its 'attributes'."

        for name, value in attributes:
            if name == "href" and re.findall(r'\A/user/+(?![B][o][o][k][m][a][n][1][9][7][4])',value):
                self.hyperlinks.append(value)
                self.is_a=1

    def get_hyperlinks(self):
        "Return the list of hyperlinks."
        return self.hyperlinks
    def end_a(self):   
        self.is_a=""   
    def handle_data(self, text):   
        if self.is_a:   
           self.name.append(text) 

   

import urllib, sgmllib, re, time

username='Bookman1974'

# Get something to work with.
url0 = r'http://www.last.fm/user/'+username
sock0 = urllib.urlopen(url0)
htmlSource0 = sock0.read()
sock0.close()
htmlSource0 = re.sub('/user/'+username+'/friends',username+'_friends_page1.html',htmlSource0,0)
htmlSource0 = re.sub('/user/'+username+'/tracks',username+'_tracks_page1.html',htmlSource0,0)
f0 = file(username+'.html', 'w')
f0.write(htmlSource0)
f0.close()


#creat a txt file to store the information of the music
ftracks = file ('tracks_info.txt','w')
ftracks.write('The Information of Music')
ftracks.write('\n')
ftracks.write('\n')

# tracks
k = 0
#set the period of the tracks
time1='2010-05-07T02:12:00Z' #t1<t<t2
time2='2010-05-07T02:13:00Z'
t1 = time.strptime(time1, "%Y-%m-%dT%H:%M:%SZ")
t2 = time.strptime(time2, "%Y-%m-%dT%H:%M:%SZ")
t=t1
numtracks=0
while t >= t1:
#retrieve the tracks start from page 1
  k=k+1
  url = r'http://www.last.fm/user/'+username+'/tracks?page='+str(k)
  sock = urllib.urlopen(url)
  htmlSource = sock.read()
  sock.close()
  tracks = MyTracks()
  tracks.feed(htmlSource)
#i is the number of the tracks in one web page
  i=0
#mypath is the basic web url
  mypath = r'http://www.last.fm'


#check whether tracks are in the period setted by user one by one
  for musictime in tracks.musictime:
    t = time.strptime(musictime, "%Y-%m-%dT%H:%M:%SZ")    
    if t<=t2 and t>=t1:
      numtracks=numtracks+1


#combine some of the tracks.name separated by & < > and other symbols 
      n=0
      m=0
      tracksname=[[]]*50
      while m<len(tracks.name):
        if tracks.name[m]=='&':
#one can use following if tracks.name contain other symbols: if tracks.name[m]=='&' or tracks.name[m]='<'
          tracksname[n-1]=tracksname[n-1]+tracks.name[m]+tracks.name[m+1]
          m=m+2
        else:
          tracksname[n]=tracks.name[m]
          m=m+1
          n=n+1


#save the information of the music
      ftracks.write("The NO."+ str(numtracks)+ " music is: ")
      ftracks.write(tracksname[i])
      ftracks.write('\n')
      ftracks.write("The time is: ")
      ftracks.write(tracks.musictime[i])
      ftracks.write('\n')
      ftracks.write("The hyperlinks is: ")
      ftracks.write(mypath + tracks.hyperlinks[i])
      ftracks.write('\n')
      ftracks.write('\n')


#save the track web and substitude the url with ".html"
      for url in tracks.hyperlinks:
        url=re.sub('\+','\\\+',url,0)
        htmlSource = re.sub(url,tracks.name[i]+'.html',htmlSource,0) 
      p=1
      for p in range(1,k):
        htmlSource = re.sub('/user/'+username+'/tracks\?page='+str(k-p),username+'_tracks_page'+str(k-p)+'.html',htmlSource,0)
        htmlSource = re.sub('/user/'+username+'/tracks\?page='+str(k+p),username+'_tracks_page'+str(k+p)+'.html',htmlSource,0)  
      f = file(username+'_tracks_page'+str(k)+'.html', 'w') 
      f.write(htmlSource)
      f.close()

#save the overall information of the track
      musicurl=re.split("\/_\/",tracks.hyperlinks[i]) 
      print musicurl  
      musicurl1=re.sub('\+','\\\+',musicurl[0],0) #substitute + with \+
      musicurl1=re.sub('\.','\\\.',musicurl1,0)   #substitute . with \.
#get the hyperlink of the tracks by splitting tracks.hyperlinks
      myurl = mypath + tracks.hyperlinks[i]
      sock1 = urllib.urlopen(myurl)
      html1 = sock1.read()
      sock1.close()
      print "save as: " + tracksname[i]+'.html'
      f = file(tracksname[i]+'.html', 'w')  
      f.write(html1)
      f.close()
      print "The "+str(numtracks)+ " music is:"+ tracksname[i]
      print username + ' '+ "listend to "+ tracksname[i] +" at:"+ tracks.musictime[i]
#save the particular of the track
      #to substitute the website
      musicinfo=['','/\+wiki','/\+images','/\+videos','/\+albums','/\+tracks','/\+events','/\+news','/\+charts','/\+similar','/\+tags','/\+listeners','/\+journal','/\+groups']
      #to name the saved website
      musicinfo2=['artist','wiki','images','videos','albums','tracks','events','news','charts','similar','tags','listeners','journal','groups']
      #to get the website url
      musicinfo3=['','/+wiki','/+images','/+videos','/+albums','/+tracks','/+events','/+news','/+charts','/+similar','/+tags','/+listeners','/+journal','/+groups']
      for j in range(0,len(musicinfo)):
        url= mypath + musicurl[0]+musicinfo3[j]
        sock = urllib.urlopen(url)
        htmlSource = sock.read() 
        sock.close()
        for s in range(0,len(musicinfo)):
          if s==0:
            htmlSource = re.sub(musicurl1+musicinfo[s]+'">Artist',tracksname[i]+' '+musicinfo2[s]+'.html'+'">Artist',htmlSource,0)
          else:
            htmlSource = re.sub(musicurl1+musicinfo[s],tracksname[i]+' '+musicinfo2[s]+'.html',htmlSource,0)
        print "  save as: " + tracksname[i] + ' '+ musicinfo2[j] 
        f = file(tracksname[i]+' '+musicinfo2[j]+'.html', 'w')  
        f.write(htmlSource)
        f.close()
    i=i+1

ftracks.write("The total number of music you selected is: "+str(numtracks))
ftracks.close()

#creat a txt file to store the list of friends
ffriends = file ('friends_list.txt','w')
ffriends.write('The List of Friends:')
ffriends.write('\n')
ffriends.write('\n')

# friends
k=1  #the number of web page
numfriend = 1
url = r'http://www.last.fm/user/'+username+'/friends?page=1'
sock = urllib.urlopen(url)
htmlSource = sock.read()
sock.close()
friends = MyFriends()
friends.feed(htmlSource)
temp = friends.name
#print temp
ffriends = file('friends_list.txt','w')
while k==1 or friends.name!=temp:
  i=0 #the number of friend in every page
  for url in friends.hyperlinks:
    htmlSource = re.sub(url,friends.name[i].lstrip(' ')+'.html',htmlSource,0)
    print i
#save the list of friends
    ffriends.write("The NO."+ str(numfriend)+ " friend is:")
    ffriends.write(friends.name[i])
    ffriends.write('\n')
    ffriends.write('\n')
    i=i+1
    numfriend = numfriend + 1
  print 'k='+str(k) 
  p=1

  for p in range(1,k):
    htmlSource = re.sub('/user/'+username+'/friends\?page='+str(k-p),username+'_friends_page'+str(k-p)+'.html',htmlSource,0)
    htmlSource = re.sub('/user/'+username+'/friends\?page='+str(k+p),username+'_friends_page'+str(k+p)+'.html',htmlSource,0)

  f = file(username+'_friends_page'+str(k)+'.html', 'w')  
  f.write(htmlSource)
  f.close()
  
  print friends.name

# Get the hyperlinks
  mypath = r'http://www.last.fm'
  n=0
  for url in friends.hyperlinks:
        myurl = mypath + url 
        print "get: " + url
        sock2 = urllib.urlopen(myurl)
        html2 = sock2.read()
        sock2.close()
    
        print "save as: " + friends.name[n].lstrip(' ')+'.html'
        f2 = file(friends.name[n].lstrip(' ')+'.html', 'w')
        f2.write(html2)
        f2.close()
        n=n+1

  k=k+1

  url = r'http://www.last.fm/user/'+username+'/friends?page='+str(k)
  sock = urllib.urlopen(url)
  htmlSource = sock.read()
  sock.close()  
  friends = MyFriends()
  friends.feed(htmlSource)
    
ffriends.write('The number of total ' + username + ' is:'+str(numfriend-1))
ffriends.close()
