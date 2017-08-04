import urllib2
from bs4 import BeautifulSoup

print "Enter Problem Code: "
s=raw_input()
site_name = "https://www.codechef.com/problems/" + s

page = urllib2.urlopen(site_name)
soup = BeautifulSoup(page, 'html.parser')

text = soup.pre.get_text()
input_text = text[:text.find('Output')]
output_text = text[input_text.find('Output'):]

print output_text
output = [int(x) for x in output_text.split() if x.isdigit()]
input = [int(x) for x in input_text.split() if x.isdigit()]

print input
print output
