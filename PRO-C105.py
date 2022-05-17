import csv
import math

with open('C105/PRO-C105/data2.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]
squared_list= []
sum =0

def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)

    mean = total / n
    return mean

for number in data:
    a = int(number) - mean(data)
    a= a**2
    squared_list.append(a)

for i in squared_list:
    sum =sum + i

result = sum/ (len(data)-1)
std_deviation = math.sqrt(result)
print(std_deviation)
