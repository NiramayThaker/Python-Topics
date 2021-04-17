with open("data_1.txt") as file_1:
    data_1 = file_1.readlines()

with open("data_2.txt") as file_2:
    data_2 = file_2.readlines()

result = [int(result) for result in data_1 if result in data_2]
print(result)
