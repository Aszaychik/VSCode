print("====INTEGER====")
data_int = 10
print("Data : ", data_int,", Data Type : ",type(data_int))


data_float = float(data_int)
data_str= str(data_int)
data_bool = bool(data_int)
print("Data : ", data_float,", Data Type : ",type(data_float))
print("Data : ", data_str,", Data Type : ",type(data_str))
print("Data : ", data_bool,", Data Type : ",type(data_bool))

print("====FLOAT====")
data_float = 10.5
print("Data : ", data_float,", Data Type : ",type(data_float))

data_int = int(data_float)
data_str= str(data_float)
data_bool = bool(data_float)
print("Data : ", data_int,", Data Type : ",type(data_int))
print("Data : ", data_str,", Data Type : ",type(data_str))
print("Data : ", data_bool,", Data Type : ",type(data_bool))

print("====BOOLEAN====")
data_bool = False
print("Data : ", data_bool,", Data Type : ",type(data_bool))

data_int = int(data_bool)
data_float = float(data_bool)
data_str= str(data_bool)
print("Data : ", data_int,", Data Type : ",type(data_int))
print("Data : ", data_float,", Data Type : ",type(data_float))
print("Data : ", data_str,", Data Type : ",type(data_str))

print("====STRING====")
data_str = "0"
print("Data : ", data_str,", Data Type : ",type(data_str))

data_int = int(data_str)
data_float = float(data_str)
data_bool= bool(data_str)
print("Data : ", data_int,", Data Type : ",type(data_int))
print("Data : ", data_float,", Data Type : ",type(data_float))
print("Data : ", data_bool,", Data Type : ",type(data_bool))

#IF String = null
data_str = ""
data_bool= bool(data_str)
print("Data : ", data_bool,", Data Type : ",type(data_bool))
