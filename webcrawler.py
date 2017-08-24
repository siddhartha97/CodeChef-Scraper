import urllib2
import subprocess
import os
import stat
from bs4 import BeautifulSoup

print "Challenge(0) or Practice(1): "
pbDomain  = raw_input()
if pbDomain:
	print "Enter Problem Code: "
	problemCode=raw_input()
	site_name = "https://www.codechef.com/problems/" + problemCode
else: 
	print "Enter Contest Code: "
	contestCode = raw_input()
	print "Enter Problem Code: "
	problemCode = raw_input()
	site_name = "https://www.codechef.com/" + contestCode + "/problems/" + problemCode

page = urllib2.urlopen(site_name)
soup = BeautifulSoup(page, 'html.parser')

pretags = soup.find_all('pre')

preText = ""

for tag in pretags:
    preText = preText + str(tag.get_text())


input_text  =  []
output_text =  []

flag_0 = 0
flag_1 = 0


#storing input and output values separately

for x in preText.split():

    if x == "Input:" or x == "Input":
        flag_0 = 1
        flag_1 = 0
        continue
    if x == "Output:" or x == "Output":
        flag_0 = 0
        flag_1 = 1
        continue
    if flag_0 == 1 and flag_1 == 0:
        input_text.append(x)
    if flag_1 == 1 and flag_0 == 0:
        output_text.append(x)


print input_text, output_text


file_1 = open("realinput.txt","w");
for x in input_text:
    file_1.write(x + "\n ")
file_1.close();

file_2 = open("realoutput.txt","w");
for x in output_text:
    file_2.write(x + "\n" )
file_2.close();

print "Enter name of your cpp file: ";
name = raw_input();

file_3 = open("run.sh" , "w");
file_3.write("#!/bin/bash" + "\n");
file_3.write("g++ " + name + "\n");
file_3.write("./a.out" + " < " + "realinput.txt" + " > " + "output.txt" + "\n");
file_3.write("g++ " + "filechecker.cpp -o check.out" + "\n");
file_3.write("./check.out"+"\n");
file_3.write("exit 0");

st = os.stat('run.sh')
os.chmod('run.sh', st.st_mode | stat.S_IEXEC)

from subprocess import call
import shlex
call(shlex.split('bash run.sh'))
call(shlex.split('bash run.sh'))
