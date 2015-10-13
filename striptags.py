from bs4 import BeautifulSoup
import urllib2
import re

#implement iterating through txt file here

x = open('urls.txt', 'r')
for line in x:

	lines = line.strip()

	content = urllib2.urlopen(lines).read()

	soup = BeautifulSoup(content)

	#formatting title
	#title = str(soup.h1).replace("\n", "").replace("<h1 class=\"title\">", "").replace("</h1>", "")
	title = str(soup.h1.text)

	#getting content from first div on page
	first_div_content = soup.find("div", class_="cards")

	#sets div_text to first_div_content, but with html tags removed
	div_text = first_div_content.text

	print div_text

	#add content to new txt file
	f = open(title + '.txt', 'w')
	#for some reason, can't print that value to text file :/
	print >> f, first_div_content
	f.close()
