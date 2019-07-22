s1=input()
tem=s1.strip()
tem1=1
for i in range (len(tem)):
 if(tem[i]==' ' and (tem[i]!=tem[i+1])):
 tem1=tem1+1
if(tem1>1):
 print(tem1)
