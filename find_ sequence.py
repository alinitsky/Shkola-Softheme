#программа поиска самой длинной непрерывной цепочки
# единиц в последовательности нулей и единиц

#считывание последовательности нулей и единиц из файла
input = open('D:\input.txt', 'r')
str = input.readline()
input.close()

# поиск самой длинной непрерывной цепочки единиц
k, max = 0, 0
a = list(str)

if a[0] == "1":
    k = k + 1
for i in range(1, len(str)):
    if a[i] and a[i-1] == "1":
        k = k + 1
    else:
        k = 0
    if k > max:
        max = k

answer = "1" * max

#запись самой длинной непрерывной цепочки единиц в файла
output = open("D:\output.txt", 'w')
output.write(answer)
output.close()
