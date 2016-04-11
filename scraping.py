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
	hoursreg=re.compile(r'<p>\n.*</p>',re.DOTALL)
	hours=hoursreg.search(resp)
	print hours.group()


hallnames=["1835-hinman", "allison", "foster-walker", "elder", "sargent", "sargent", "willard"]
cafenames=["einsteins", "frans", "lisas", "express"]

respo="""<div class="accordionBody">
<p>Week of: 04/04/2016 - 04/10/2016</p>
<p style="text-decoration:underline;">Allison Standard Hours</p>
<p>
Monday - Friday: 7:30 a.m. - 7:00 p.m.<br/>
Saturday - Sunday: 11:00 a.m. - 7:00 p.m.<br/>
</p>
</div>"""
parseresponse(respo)

