# Functions

# Function to add two numbers
def add(x,y):
  return x + y

# Function to subtract two numbers
def sub(x,y):
  return x - y

# Function to multiply two numbers
def mul(x,y):
  return x * y

#Function to divide two numbers
def div(x,y):
  return x / y

# User options menu
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take input from the user
while True:
  choice = input("Enter choice(1/2/3/4): ")
  
  # Check if choice is one of the four options
  if choice in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Invalid input. Please enter a number.") 
      continue

# One equal sign assigns a value to a variable
# Two equal signs check if two values are equal
    if choice == '1':
      print(num1, "+" ,num2, "=", add(num1, num2))
    elif choice == '2':
      print(num1, "-", num2, "=", sub(num1, num2))
    elif choice == '3':
      print(num1, "*", num2, "=", mul(num1, num2))
    elif choice == '4':
      if num2 == 0:
        print("Error! Cannot divide by zero.")
      # remember, division by 0 is not possible

# Check if user wants to continue or not
    next = input("Do you want to do another calculation? [yes/no]: ")
    if next == "no":
        break
    if next == "yes":
        continue
    else:
        print("Invalid Input")