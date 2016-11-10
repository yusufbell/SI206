# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import requests
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
html = urllib.request.urlopen(base_url)
#r = requests.get(base_url)
soup = BeautifulSoup(html, "html.parser")
html_doc = soup.prettify()
html_doc = html_doc.replace('student', 'AMAZING student')
html_doc = html_doc.replace('https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_', 'media/logo.png')
html_doc = html_doc.replace('logo2.png', 'media/logo.png')
fout = open('yusufb.html', 'w')
fout.write(html_doc)
fout.close()



