numbers = [1,56,234,87,4,76,24,69,90,135]
even_number = [x for x in numbers if x%2 == 0]
print(even_number)

print("x"*20)

positive_numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive = [x for x in positive_numbers if x>0]
print(positive)

print("x"*20)

words = ["hello", "my", "name", "is", "Sam"]
for word in words:
    print(f"({word}, {len(word)})")
