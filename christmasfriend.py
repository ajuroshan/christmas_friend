import random
import csv

csv_filename = 'names.csv'

with open(csv_filename) as f:
    reader = csv.DictReader(f)
    Data = {"Name": [], "Phone": [],  "Branch": []}
    for record in reader:
        Data["Name"].append(record["Name"])
        Data["Branch"].append(record["Branch"])
        Data["Phone"].append(record["Phone"])

with open(csv_filename) as f:
    reader = csv.DictReader(f)
    realData = list(reader)


number_list1 = []
number_list2 = []
number_list3 = []


for i in range(0, len(Data["Phone"])):
    number_list1.append(Data["Phone"][i])
    number_list2.append(Data["Phone"][i])
    number_list3.append(Data["Phone"][i])


# List after first shuffle
random.shuffle(number_list1)
shuffle_1 = number_list1

# List after second shuffle
random.shuffle(number_list2)
shuffle_2 = number_list2

result = []
for i in range(0 , len(number_list1)):
    result.append([shuffle_1[i], shuffle_2[i]])

dictionary = {}
for i in range(len(number_list3)):
    dictionary[number_list3[i]] = realData[i]

print(dictionary)