import math

def newSquareCount(a,b):
	if a > b:
		print a
		k=a
	else:
		print b
		k=b
		
	z=k*(k+1)*(2*k+1)/6+math.fabs(a-b)*k*(k+1)/2
	
	return z
	
print newSquareCount(5,3)