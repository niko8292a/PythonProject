# Variable = A container for a value (string, integer, float, boolean)
#            A Variable behaves as if it was the value it contains

#String
#name = "Nikolaj"
#favorite_food = "Pizza"
#email = "Nikolaj.englert.dk@icloud.com"

#integers
#age = 15
#quantity = 3
#num_of_students = 24

#Float
#price = 19.95
#gpa = 3.2
#distance = 1.5

#booleans
#is_student = True
#for_sale = False
#is_online = True


# Typecasting = the process of converting a variable from one data type to another
#               str(bogstaver eller tal som fungere som ord), int(tal som fungere som tal), float(decimal tal), bool(true or false)

#print(type(name))
#print(type(age))
#print(type(gpa))
#print(type(is_student))

# Change variable
#gpa = int(gpa)

#print(gpa)

# input() = A function that prompts the user to enter data
#           returns the entered data as string

#real_name = input("Enter your name: ")
#real_age = input("Enter your age: ")
#real_gpa = input("Enter your GPA: ")

#real_age = int(real_age)
#real_age = real_age + 1

#print(f"Your {real_name}, you'll be {real_age} years old next year and your GPA is {real_gpa}")

#length = float(input("Enter the length of the rectangle --> "))
#width = float(input("Enter the width of the rectangle --> " ))
#area = length * width

#print(f"the area is {area}cm")

#item = input("What item would you like to buy? ")
#price = float(input("How much does that item cost? "))
#amount = int(input("How many of that item would you like? "))

#total = price * amount

#print(f"You have bought {amount} x {item}")
#print(f"Your total is ${total}")


# Mad libs game
# word game where you create a story
# by filling in blanks with random words

#adjective1 = input("Enter adjective (description): ")
#noun1 = input("Enter noun (person, place, thing): ")
#adjective2 = input("Enter adjective (description): ")
#verb1 = input("Enter verb ending with 'ing: ")
#adjective3 = input("Enter adjective (description): ")

#print(f"Today i went to a {adjective1} zoo.")
#print(f"In an exhibit, i saw a {noun1}")
#print(f"The {noun1} was {adjective2} and {verb1}")
#print(f"I was {adjective3}")



# friends = 10

# friends = friends + 1       friends plus 1
# friends += 1
# friends = friends - 2       friends minus 2
# friends -= 2
# friends = friends * 3       friends gange 3
# friends *= 3
# friends = friends / 2       friends divideret med 2
# friends /= 2
# friends = friends ** 2      friends ganget med sig selv 2 gange
# friends **= 2
# remainder = friends % 3     hvis "friends" bliver delt op i 3 grupper så er der remainder tilbage

# print(friends)

# to round up/down
#x = 9.9
#y = 4
#z = 5

# result = round(x)       rund op eller ned til det tætteste
# result = abs(y)         hvor mange tal y er væk fra 0
# result = pow(y, z)      y ganget med sig selv z gange
# result = max(x, y, z)   det største tal mellem x, y, z
# result = min(x, y, z)   det mindste tal mellem x, y, z

# print(result)



# print(math.pi) print matematisk konstant pi
# print(math.e)
# result = math.sqrt(x)  kvadrat roden af x
# result = math.ceil(x)  x rundet op
# result = math.floor(x) x rundet ned


#import math

#radius = float(input("Enter the radius of the circle: "))

#circumference = 2 * math.pi * radius

#print(f"The circumference of the circle is {round(circumference, 2)}cm.")

#import math

#radius = float(input("Enter the radius of a circle: "))
#area = math.pi * pow(radius, 2)

#print(f"The area of a circle is {round(area, 2)}cm^2")


#import math                           Pythagoras theory

#a = float(input("What is the length of line A? "))
#b = float(input("What is the length of line B? "))

#hypotenuse = math.sqrt(a**2 + b**2)

#print(f"The hypotenuse is {round(hypotenuse, 2)}")


# if = Do some code IF some condition is true
#      Else do something else

#age = int(input("Enter your age: "))

#if age >= 18:
#    print("You are old enough to vote!")
#elif age < 0:
#    print("You haven't been born yet!")
#else:
#    print("You are not old enough to vote!")

Dette er skrevet på laptop