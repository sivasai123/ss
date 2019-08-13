a,b,c=map(int,input().split())
sum=b+c
a=a/2
temp=a
while(a!=0 and ((a>b) and (a>c))):
	a=a-sum
a=temp-a
while(a!=0 and ((a>b) and (a>c))):
	a=a-sum
if(a==0):
	print('YES')
else:
	print('NO')
