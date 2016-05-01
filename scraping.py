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

# def fromnaturallang(resp):

hallnames=["1835-hinman", "allison", "foster-walker", "elder", "sargent", "sargent", "willard"]
cafenames=["einsteins", "frans", "lisas", "express"]

for hn in hallnames:
	resp=str(scrapeapage(True, hn))
	presp=parseresponse(resp)
	print presp
