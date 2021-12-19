data_integer = 10
print("Data : ", data_integer,", Data Type : ",type(data_integer))

data_float = 10.5
print("Data : ", data_float,", Data Type : ",type(data_float))

data_string = "AGOES"
print("Data : ", data_string,", Data Type : ",type(data_string))

data_bool = True
print("Data : ", data_bool,", Data Type : ",type(data_bool))

data_complex = complex(20,116)
print("Data : ", data_complex,", Data Type : ",type(data_complex))

from ctypes import c_double
data_c_double = c_double(11.20)
print("Data : ", data_c_double,", Data Type : ",type(data_c_double))