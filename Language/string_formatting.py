name = "Ayush"
country = "India"

# Method 1
letter = "My Name is {} and i am from {}"
print(letter.format(name, country))

letter = "I am from {1} and my Name is {0}"
print(letter.format(name, country))

# Method 2
print(f"my name is {name} and i am from {country}")

#Number Roundoff
text = "For only {price:.2f} ruppes"
print(text.format(price = 49.0999999))

#Number Roundoff
price = 49.0999999
text = "For only {price:.2f} ruppes"
print(text)

#number as string 
print(type(2 * 30))
print(type(f"{2*30}"))
num = 10
print(type(num))
print(type(str(num)))