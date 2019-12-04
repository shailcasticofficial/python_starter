a = 2       # simple code
b = 10
sum = a+b
print(sum)
multi = a*b
print(multi)
divide = a/b
print(divide)
subtract = a-b
print(subtract)
modes = a//b
print(modes)
# this is the new python file for the class
'''
this is th new file for the class
'''
print("hello world")
print('hello shailesh')
print('happy learning \n\n "welcome" to the system')
a = 10   # integer
b = '"data science"'   # string
print(a, b)
print(a)
print(b)
x, y, z = 10, 20, 30
print(x, y, z)
print(x)
print(y)
print(z)

A = 16
B = 12
C = 'python'
print(A, B, C)
# standard data types
# immutable data types
# numbers
a = 10             # integer
b = 20.10         # float
c = 20+4j          # complex numbers
d = 10+9j
print(d-c)
print(a, b)
# strings
a = 'welcome shailesh'
b = 'python is great'
print(a)
print(b)
# tuples
a = (1, 2, 3, "python for data science")
print(a)
list = (1, 2, 4, 5, 6)
print(list)
print(list[0])
print(list[2])
print(list[3])
demo = (1, 2, 3, 4, 5, [4, 5, 6])       # a list inside the tuple
print(demo)
print(demo[0])
print(demo[5][0])
# mutable data type
# lists
z = [1, 2, 3, 4, 'python!', 'data science!']
print(z)
print(z[0])
print(z[4])
print(z[5])
z[2] = 'change second element'
print(z)
d = [1, 2, 5, 6, 'data science', (2, 5, 6)]    # a tuple inside the list
print(d)
d[4] = 'data'
print(d)
print(d[5][2])
# dictionaries
f = {'name': 'shailesh', 'age': 25}
print(f)
# sets
g = {1, 2, 12, 1, 2, 2, 2, 2, 1, 2, 2, 2}
print(g)
# python operators
# arithmetic
a = 55
b = 10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a % b)
# identity operators
c = 25
d = 28
print(c is not d)
print(c is d)
today = 'wednesday'
yoga_day = 'thursday'
print(today is yoga_day)
# membership checking
run = [4, 5, 6]   # list
print(5 in run)
print(8 not in run)
den = (4, 5, 6)    # tuples
print(4 in den)
print(9 not in den)
fun = {'age': 14, 'city': 'kutch'}    # dictionary
print(fun['age'])
print('city' in fun)
# conditional statement
# if
x = 25
y = 25
if(x<y):
    print("x is less then y")
elif(x>y):
    print("x is greater then y")
else:
    print("x and y are equal")
# if else statement
a = 45
if(a<10):
    print("less then 10")
if(10<=a<25):
    print(" in between 10 and 25")
else:
    print("greater then 25")
# if elif else
marks = 40
if(marks<=40):
    print("fail")
elif(40<marks<=60):
    print("average")
else:
    print("congratulation you got distinction")
# loops
# types of loops while for nested
# while forward
count = 0
while(count<15):
    print(count)
    count = count+1

print("good bye!")

# while "backward"
count=15
while(count>0):
    print(count)
    count=count-1
print("good bye!")
# for loop    "to create factorial of a number"
vegetables = ['lady finger', 'cauliflower', 'pumpkin', 'spinach', 'soda', 'pepsi']
for vegetable in vegetables:
    print(vegetable)
# example
list1 = [1, 2, 3, "python file"]

for i in list1:
    print(i)   # to calculate the factorial of a number
# nested loops " a loop inside a loop"
count = 1
for i in range(10):
    print(str(i)*i)
    for j in range(0, i):
        count = count+1
# loop control statement  break continue pass
for i in range(1, 11):
    print(i)
    if i == 5:
        continue
        # break
      # pass
print(i)
