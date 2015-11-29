import sys
import math

def Kai(x):
	if x ==0:
		return 1
	value = 0
	if x == 1:
		value = 1
	else:
		value = x * Kai(x-1)
	return value

def Closoid(tau):
	A = 1
	k = 1
	x = 0
	x_1 = 2
	F_k_x = 0
	F_k_y = 0
	temp_f = 2
	while(math.fabs(temp_f-F_k_x) > 0.00001):
		temp_f = F_k_x
		f_1 = math.pow(-1,k-1)
		f_2 = 1.0/(Kai(2*(k-1))*(4*k-3))
		f_3 = math.pow(tau,2*(k-1))
		F_k_x += f_1*f_2*f_3
		k = k+1
		#print "%s %s %s" %(f_1,f_2,f_3)
		#print F_k_x
	temp_f = 2
	k = 1
	while(math.fabs(temp_f-F_k_y) > 0.00001):
		temp_f = F_k_y
		f_1 = math.pow(-1,k-1)
		f_2 = 1.0/(Kai(2*k-1)*(4*k-1))
		f_3 = math.pow(tau,2*(k-1))
		F_k_y += f_1*f_2*f_3
		k = k+1
		#print "%s %s %s" %(f_1,f_2,f_3)
		#print F_k_y
	n =[1,1]
	n[0] = F_k_x*A*math.sqrt(2*tau)
	n[1] = F_k_y*A*tau*math.sqrt(2*tau)
	return n
def Formula(x):
	point = Closoid((math.pi/60)*x)
	n = [point[0]*100,point[1]*100]
	return n
