name = input("what is your name? ")

age = input("what is your age? ")

intage = int(age)

y = "years" if intage > 1 else "year"

if intage <= 0:
    print("You have entered a wrong age, you can't play game")

elif intage > 0  and intage <= 12:

    print("Hello " + name + " you're a child  of age " + age + " " + y + " old." )


elif intage >= 13 and intage <= 19 :

    print("Hello " + name + " You're a Teenage of age " + age + " " + y + " old.")

else:
     
    print("Hello " + name + " you're an adult of age " + age + " " + y + " old and you shounld'nt be writting this kind of code ")

# print("hello " + name + " you are " + age +  " " + y + " old")