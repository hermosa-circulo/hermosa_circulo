#!/usr/bin/python
import os
import cgi
import cgitb
import sys
import codecs
import makeobj
import time
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
wheel_radius=int(data["wheel_radius"].value)
begining_point = int(data["begining_point"].value)
begin = 100 - int(data["begin"].value)
point_num = int(data["point_num"].value)
breast_wide = 1 - float(data["breast_wide"].value)
ret = makeobj.make(wheel_radius,begining_point,begin,point_num,breast_wide)

file = open('model2.obj','w')
file.write(ret)
file.close()
print ret;
