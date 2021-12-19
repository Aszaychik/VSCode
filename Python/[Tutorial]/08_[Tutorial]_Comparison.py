print("====NUMBER COMPARISON====")
a = int(input("Input data a : "))
b = int(input("Input data b : "))

result = a > b
print(a,">",b,"=",result)

result = a < b
print(a,"<",b,"=",result)

result = a >= b
print(a,">=",b,"=",result)

result = a <= b
print(a,"<=",b,"=",result)

result = a == b
print(a,"==",b,"=",result)

result = a != b
print(a,"!=",b,"=",result)

print("Data a = ",a,", Id = ",hex(id(a)))
print("Data b = ",b,", Id = ",hex(id(b)))

result = a is b
print("a is b =",result)

result = a is not b
print("a is not b =",result)