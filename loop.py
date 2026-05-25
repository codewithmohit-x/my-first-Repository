#ranges
#10 - 100
#23 - 56
#67 - 78
#56

range(10, 101, 1)
#range(jha se start, jha tak + 1, jump)
range(23, 57, 1)
range(67, 79, 1)
range(57)

for i in range(10, 101, 10):
    print(i)


a = "mohit gangwar"
print(len(a))

for i in range(0, len(a), 1):
    print(i)
# 0 1 2 3 4 5 6 7 8 9 10 11 12


for i in range(0, len(a), 1):
    print(a[i])
# m o h i t   g a n g w a r


for i in range(0, len(a), 1):
    print(f"{i} : {a[i]}")




#break
for i in range (1, 11):
    if i == 4 :
        break
    print(i)



#continue
for i in range (1, 11):
    if i == 4 :
        continue
    print(i)

