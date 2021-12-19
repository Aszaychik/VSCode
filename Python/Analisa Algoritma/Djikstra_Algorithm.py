import math

print("======================================== \n\n")
print("UNIVERSITAS ISLAM LAMONGAN 2021\n\n")
print("PROGRAM ALGORITMA DIJKSTRA \n\n")
print("======================================== \n\n")

ver = int(input("Masukkan Jumlah Vertex yang Anda inginkan : "))

weight = [ver][ver]
buff = [ver]
path = [ver]
prev = [ver]
visited = [ver]

for i in range(1, ver):
    buff[i] = math.inf
    prev[i] = -1
    path[i] = 0
    for j in range(1, ver):
        weight[i][j] = math.inf
for i in range(1, ver):
    for j in range(i+1,ver):
        weight[i][j] = int(input("Masukkan bobot ",i,"ke",j,":"))
        weight[j][i] = weight[i][j]

source = int(input("Masukkan Vertex Awal : "))
target = int(input("Masukkan Vertex Tujuan : "))

start = source
visited[start]= 1
buff[start] = 0

while visited[target] == 0:
    minimum = math.inf
    m = 0
    for i in range(1, ver):
        update = buff[start] + weight[start][i]
        if update < buff[i] and visited[i] == 0:
            buff[i] = update
            prev[i] = start

        elif minimum > buff[i] and visited[i] == 0:
            minimum = buff [i]
            m = 1

    start = m
    visited[start] = 1

min_weight = buff[target]
start = target
j = 0
while start != -1:
    path[j] = start
    start = prev[start]

print("\nBobot terkecil yang dilalui adalah ",min_weight,"\n")
print("Jalur yang ditempuh adalah : ")
for i in range(0,ver-1,-1):
    if path[i] != 0:
        print(path[i]," ")

print("TERIMA KASIH, SELAMAT MENCOBA\n\n")