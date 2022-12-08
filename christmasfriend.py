import random
import csv

csv_filename = 'names.csv'

with open(csv_filename) as f:
    reader = csv.DictReader(f)
    Data = {"Name": [], "Phone": [],  "Branch": []}
    for record in reader:
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

correctData = {}
for i in range(len(number_list3)):
    correctData[number_list3[i]] = realData[i]


shuffledData = {}
for i in range(len(number_list2)):
    shuffledData[number_list2[i]] = realData[i]


# initializing dictionary
test_dict = {"gfg": 1, "is": 7, "best": 8,
             "for": 3, "geeks": 9}

# printing original dictionary
print("The original dictionary is : " + str(correctData))

# shuffling values
temp = list(correctData.values())
random.shuffle(temp)

# reassigning to keys
res = dict(zip(correctData, temp))

# printing result
print("The shuffled dictionary : " + str(res))

my_list = list(res.values())

field_names = ['Timestamp', 'Name', 'Branch', 'Phone', 'Password']

with open('FinalResult.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(my_list)



