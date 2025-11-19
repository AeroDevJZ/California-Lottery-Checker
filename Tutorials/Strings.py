course = "Python programming"
# returns length of the string
print(len(course))

# returns first character in string
print(course[0])

# returns the last character in string
print(course[-1])

# returns the substring from 0 to 3 exclusive to 3
print(course[0:3])

# returns new string the same as old string
print(course[0:])
print(course[:])

# python puts 0 in automatically
print(course[:3])

# ------------------------------------------------------------------------------------------------------------------------------------------

# \ tells python to ignore what comes after command wise and it treats it like a string (called escape sequence)
course1 = "Python \"Programming"
print(course1)

# \n tells python to skip to next line
course2 = "Python \nProgramming"
print(course2)

# ------------------------------------------------------------------------------------------------------------------------------------------

first = "Mosh"
last = "Hamedani"

# curly braces in a string have the same effect as concatination
full = first + " " + last
print(full)
# "f" allows for embeded expressions via variables through {} rather than concatination
full = f"{first} {last}"
print(full)

# ------------------------------------------------------------------------------------------------------------------------------------------

# use dot notation to access methods in the object
print(course.upper())
print(course.lower())
print(course.title())

# use strip to remove spaces from both sides, lstrip() from only left and rstrip() from only right
course3 = "    python programming  "
print(course3.strip())

# use the find method to find a substring in the larger string, returns number of first character searched, -1 if none found

print(course.find("pro"))
print(course.find("o"))
print(course.replace("p", "j"))
print(course.replace("m", ""))

# boolean true or false
print("pro" in course)
print("swift" not in course)

# length of string
print(len(course))
