numbers = [1,56,234,87,4,76,24,69,90,135]
for number in numbers:
    if number % 2 == 0:
        print(number)


numbers = [1,56,234,87,4,76,24,69,90,135]
odd_numbers = filter((lambda x: x % 2 != 0), numbers)
print(list(odd_numbers))

