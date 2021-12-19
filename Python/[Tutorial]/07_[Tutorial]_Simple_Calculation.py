print("====Convertion Program====")

data_inch = int(input("Input Inch : "))

print("Choose Convertion : ")
print("1.Inch to cm\t2.Inch to m\t3.Inch to ft\t4.Inch to yrd")
inch_to = int(input())

inch_to_cm = data_inch*2.54
inch_to_m = data_inch*0.0254
inch_to_foot = data_inch*(1/12)
inch_to_yard = data_inch*(1/36)

if inch_to == 1:
    print(data_inch,"inch = ",inch_to_cm,"cm")
elif inch_to == 2:
    print(data_inch,"inch = ",inch_to_m,"m")
elif inch_to == 3:
    print(data_inch,"inch = ",inch_to_foot,"ft")
else:
    print(data_inch,"inch = ",inch_to_yard,"yrd")