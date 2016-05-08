from bs4 import BeautifulSoup
import csv
import webbrowser
import urllib
import re

def scrapeapage(isdininghall, hallname):
	opener=urllib.FancyURLopener({})
	if isdininghall:
		url="https://northwestern.sodexomyway.com/dining-choices/resident/"+hallname+".html"
	else: 
		url="https://northwestern.sodexomyway.com/dining-choices/retail/"+cafename+".html"
	openerFile = opener.open(url)
	htmlFile = openerFile.read()
	soup = BeautifulSoup(htmlFile,"html.parser")
	data = soup.find_all("div", "accordionBody")
	response=str(data[2])
	return response
	
def parseresponse(resp): 
	hoursreg=re.compile(r'<p>.*<\/p>',re.DOTALL)
	hours=hoursreg.search(resp)
	hours=hours.group()
	# found the paragraph with hours using regex
	hours=hours.split('<p>')[2].split('\n')[1:3]
	# split hours on new lines
	for i,j in enumerate(hours): 
		bropen=0
		for a,b in enumerate(j):
			if b=='<':
				bropen=a
		hours[i]=hours[i][0:bropen]
	# #removed line breaks
	return hours

def hrstosecs(hrs):
	hour=hrs.split(':')[0]
	mins=hrs.split(':')[1].split(' ')[0]
	amorpm=hrs.split(' ')[1].split('.')[0]
	secs=int(hour)*3600+int(mins)*60
	if amorpm=='p':
		secs+=43200
	return int(secs)

def gethallrawtime():
	"""returns a list of lists of all hall times where a hall time is in format:
	[hallname,1setofdays,2setofdays(optional),...] where set of days is a list in format:
	[[startday,endday(optional)],[starttime(secs),endtime(secs)]]"""
	hallnames=["1835-hinman", "allison", "foster-walker", "elder", "sargent", "sargent", "willard"]
	cafenames=["einsteins", "frans", "lisas", "express"]
	daydict={'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6,'Sunday':0}
	allhalls=[]
	for hn in hallnames:
		halldeets=[]
		resp=str(scrapeapage(True, hn))
		print hn
		halldeets.append(hn)
		presp=parseresponse(resp) #List of sentences like: ['Monday - Friday: 11:00 a.m. - 7:00 p.m.', 'Saturday - Sunday: Closed']
		for s in presp:
			sentence=[]
			dayreg=re.compile(r'[A-Z,a-z]{3,5}day')
			days=dayreg.findall(s) #got a list of the days
			print "days"
			print days
			for iday in range(len(days)):
				days[iday]=daydict.get(days[iday],False)
			sentence.append(days)
			timereg=re.compile(r'\d{1,2}:\d{1,2}\s[a,p].m.')
			time=timereg.findall(s) #got a list of times
			print "time"
			print time
			if time==[]:
				time=[0,0]
			else:
				start=hrstosecs(time[0])
				end=hrstosecs(time[1])
				time=[start,end]
			print time
			sentence.append(time)
			halldeets.append(sentence)
		allhalls.append(halldeets)
		print "-------------"
	return allhalls

def tojson(allhalls):
	"""a function that will take in a list as returned by gethallrawtime() and create a json"""
	print "to be implemented..."









