#!/usr/bin/python
import os
import cgi
import cgitb
import sys
import codecs
import time
import random
#print "Location: http://ec2-54-148-249-100.us-west-2.compute.amazonaws.com/mrdoob-three.js/index.html\n\n"
print "Content-type: text/html\n\n";
print "<html>\n<body>\n";
print "<div style =\"width: 100%; font-size: 40px; font-weigth: bold; text-align: center;\">\n";
print "CGI TEST";
print "\n</div>\n";
print "</body>\n</html>\n";

if os.environ['REQUEST_METHOD'] == 'POST':
	print 'POST REQUEST'
data = cgi.FieldStorage()
osize=data["wheel_radius"].value
#b =data["begining_point"].value
x = data["begin"].value
y = data["point_num"].value
z = data["breast_wide"].value

ret = random.random()
print ret;
file = open('change.txt','w')
#str_temp = ret+"\n"
file.write(str(ret)+"\n")
file.write(osize+"\n")
file.write(x+"\n")
file.write(y+"\n")
file.write(z+"\n")
file.close()
print ret;
