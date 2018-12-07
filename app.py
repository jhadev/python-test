import math

print("python")
print("python " * 10)

x, y = 1, 2
z = 16
unit_price = 3

print(unit_price * y * z)

students_count = 1000
print(type(students_count))

rating = 4.99
print(type(rating))

is_published = False
print(type(is_published))

course_name = """Python
Programming"""

print(type(course_name))

print(len(course_name))
print(course_name[0:3])
print(course_name[-2])

first = "Joe"
last = "Boxer"
full = f"{first} {last}"
print(full)

o = y ** 10
print(o)


# comment
# \" escape sequences
# \'
# \\
# \n

# uppercase variables to tell others its a constant
PI = 3.14159265359
print(math.floor(PI))

p = (math.ceil(PI))
print(p)

b = input("x: ")

print(int(b))
print(float(b))
print(bool(b))
