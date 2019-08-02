i=0
X,Y=map(int,input().split())
Z=list(map(int,input().split()))[:X]
for k in Z:
    	if k==Y:
		       i+=1
if(i!=0):
	    print('yes')
else:
	    print('no')
