def too_old(x,y): return x+y > 30
age = [22,25,29,34,56,24]
age1 = [13,1,2,34,56,23]
m = filter (too_old, age + age1)
print(m)