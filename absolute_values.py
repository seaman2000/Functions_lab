list_of_numbers = input().split()

absolute_values = []

for num in list_of_numbers:
    absolute_values.append(abs(float(num)))

print(absolute_values)