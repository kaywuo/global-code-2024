# def too_old(x): return x > 30
# age = [22,25,29,34,56,24,12]
# m = filter(too_old, age)
# print(list(m))

data = [(25,1),(17,3),(100,2),(24,4)]
def acceptance_students(x):
    age, level = x
    return(age>25) and (level>= 2)
n = filter(acceptance_students,data)
print(list(n))


items = [1,2,3,4,5,7]
squares = map(lambda x:x**2, items)
k = squares
print(list(k))
