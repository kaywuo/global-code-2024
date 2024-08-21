name = input("what is your name? ")
age = input("what is your age? ")
y = "years" if int(age) > 1 else "year"
print("hello " + name + " you are " + age +  " " + y + " old")