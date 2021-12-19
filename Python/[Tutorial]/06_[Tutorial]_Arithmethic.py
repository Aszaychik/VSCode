a = 11
b = 2

result = a + b
print(a,"+",b,"=",result)

result = a - b
print(a,"-",b,"=",result)

result = a * b
print(a,"*",b,"=",result)

result = a / b
print(a,"/",b,"=",result)

result = a ** b
print(a,"**",b,"=",result)

result = a // b
print(a,"//",b,"=",result)

x = 6
y = 4
z = 2

result = x ** y * z + x / y - y % z // x
print(x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x," = ",result)

result = x + y * z
print(x,"+",y,"*",z," = ",result)
result = (x + y) * z

print("(",x,"+",y,")",'*',z," = ",result)