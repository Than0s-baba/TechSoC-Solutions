x=101
pali =0
k=x
while x>0:
    pali=int(pali*10+x%10)
    print(pali)
    x=int(x/10)
print(pali)
print(k)
print(pali==k)
### pascal's triangle#############################################################################################
# import math
# lines=int(input("enter number of rows required"))
# temp=[]
# for i in range(lines):
#     for j in range(i):
#         temp.append(math.factorial(i)/(math.factorial(j)*math.factorial(i-j)))
#     print(temp)
#     temp=[]