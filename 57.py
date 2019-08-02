i=0
A,B=map(int,input().split())
c=list(map(int,input().split()))[:A]
for k in c:
	if k==B:
		i+=1
print(i)
