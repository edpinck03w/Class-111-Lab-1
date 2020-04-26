

def separator():
    print('_____________')
    print('inside')
print('Hello World!')

# data types
name = "Edward"
last = "Pinckney"
age = 34
found = False
average = 2.34


print(name)
print(average)
print(found)

# operations
print(21 +21)
print(100 - 50)
print(12 * 321)
print(100/10)
print(10 % 3) # % = module operator (gives the residue)

print(name + name)
print(age + age)



print('outside')

separator()

if(age < 90):
    print('You are still young')
elif (age == 90):
    print('You are on the border line')
else: 
    print('Sorry bud, you are getting old :) ')