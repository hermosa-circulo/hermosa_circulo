import os
a = 0
Load = "ok"
while a==0:
	fp = open("change.txt",'r')
	temp = fp.readlines()
	for i in range(len(temp)):
		temp[i] = temp[i].rstrip()
	if Load != temp[0]:
		Load = temp[0]
		str_temp = "blender --background --python Lattice.py "+temp[1]+" "+temp[2]+" "+temp[3]+" "+temp[4]
		os.system(str_temp)
		print str_temp
	fp.close()
