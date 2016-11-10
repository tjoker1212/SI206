# Use http://collemc.people.si.umich.edu/data/bshw3StarterFile.html as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import re

url = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
openurl = urllib.request.urlopen(url).read()

soup = BeautifulSoup(openurl, "html.parser")





img = soup("img")
print (len(img))
for tag in img:

	x = tag['src']
	
	if x == "logo2.png":
		tag['src'] = "logo.png"
	else:
		tag['src']= "IMG_2217.JPG"

string = (soup.prettify())
print (len(string))
new_soup = (string.replace("student", "AMAZING student"))

h = open("BS.html", "w")
h.write(new_soup)
h.close()