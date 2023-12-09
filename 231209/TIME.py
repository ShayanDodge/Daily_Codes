import time
start_time =  time.time()

list = []

for i in range(10000000):
    list.append(i)

end_time = time.time()

# print(list)
print(end_time - start_time)
