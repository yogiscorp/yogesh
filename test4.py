def getvalues(a,pi=3.141, c=None):
	if c is not None:
		print(c)
		return a+pi+c
	return a+pi

def getsum(a,b):
    return a+b
def getdifference(a,b):
	if isinstance(a,float):
		return a-b
	else:
		print ("pass either int or float to perform this operator") 
print("hi")
if __name__=='__main__':
    a=2.5
    b=1.2
    #print(getsum(a,b))
    #print(getdifference(a,b))
    print (getvalues(4,10))