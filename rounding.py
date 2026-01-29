numbers = input().split()
list_of_numbers = []

for each_number in numbers:
    float_number = float(each_number)
    list_of_numbers.append(round(float_number))

print(list_of_numbers)