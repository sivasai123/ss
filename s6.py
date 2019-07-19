n = int(input(" "))
n1 = n
a = 0
while n != 0:
    r = n % 10
    a = a + r ** 3
    n = n // 10
if s == n1:
    print("Yes")
else:
    print ("No")
