# This is test project

print(str(2) + 'hello')
x = 2
print(type(x))
x = 'Yamini'
print(type(x))
s = "Hi, {}"
print(s.format(x))
s = "Hi, {} and {}"
print(s.format(x,100))

s = "Hi, {1} and {0}"
print(s.format(x,100))

print("Hi, {1} and {0}".format(x,100))