print("====Convertion Program====")

data_inch = int(input("Input Inch : "))

inch_to_cm = data_inch*2.54
inch_to_m = data_inch*0.0254
inch_to_foot = data_inch*(1/12)
inch_to_yard = data_inch*(1/36)

print(data_inch,"inch = ",inch_to_cm,"cm")
print(data_inch,"inch = ",inch_to_m,"m")
print(data_inch,"inch = ",inch_to_foot,"ft")
print(data_inch,"inch = ",inch_to_yard,"yrd")