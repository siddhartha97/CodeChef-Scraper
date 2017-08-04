import urllib2
from bs4 import BeautifulSoup

print "Enter Problem Code: "
str_1=raw_input()
site_name = "https://www.codechef.com/problems/" + str_1

page = urllib2.urlopen(site_name)
soup = BeautifulSoup(page, 'html.parser')

pretags = soup.find_all('pre')

str_2 = ""

for tag in pretags:
    str_2 = str_2 + str(tag.get_text())

#print str_2     # stores all the pre codes.

input_text  =  []
output_text =  []

flag_0 = 0
flag_1 = 0


#storing input and output values separately

for x in str_2.split():
    if x == "Input:":
        flag_0 = 1
        flag_1 = 0
        continue
    if x == "Output:":
        flag_0 = 0
        flag_1 = 1
        continue
    if flag_0 == 1 and flag_1 == 0:
        input_text.append(x)
    if flag_1 == 1 and flag_0 == 0:
        output_text.append(x)


print input_text, output_text
