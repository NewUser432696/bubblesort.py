buble
data = [18,7,6,19,4,24,12,11,10,1]
print("data sebelum diurutkan :", data)
banyak_data = len (data)

for i in range (banyak_data-1):
    for j in range (banyak_data-1) :
        if data [j]>data[j+1] :
            temp = data [j]
            data [j] = data [j+1]
            data [j+1] = temp
print ("data setelah diurutkan:", data)

data = [18,7,6,19,4,28,12,15,10,1,30,50,22,15,18,86,95,70,65,44,21,35,99,20,25,19,13,18,17,35,84,29,58,70,71,78,51,38,90,44,67,77,88,22,56,34,88,71,23,66]
print("data sebelum diurutkan :", data)
banyak_data = len (data)for i in range (banyak_data-1):
    for j in range (banyak_data-1) :
        if data [j]>data[j+1] :
            temp = data [j]
            data [j] = data [j+1]
            data [j+1] = temp
print ("data setelah diurutkan:", data)
