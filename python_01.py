#Declare variables and data types
name="Sunjida" 
age=23
GPA=3.5
is_student=True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

#Type Conversions
num_str="123" #String to integer
num_int=int(num_str)
print(num_int)

num = 456 #Integer to string
num_str2 = str(num)
print(num_str2)

flt = 3.99 #Float to integer
converted = int(flt)
print(converted)     #.99 is removed

print(bool(1))  #Integer to boolean  #1=True
print(bool(0))  #0=False

#operators
a = 17 #given
b = 5

print(a+b)   #Addition 
print(a-b)    #Subtraction
print(a*b)    #Multiplication
print(a / b)    #Division

print(a//b)   #Floordivision
print(a%b)    #Modulus

print(a ** b)   #Power

print(a>b)
print(a==b)
print(a!=b)

#String Manipulation
name="python programming"

print(name.upper())
print(name.title())
print(name.replace("programming", "language"))
print(len(name))

#Using f-string
name="Sunjida"
age=23
gpa=3.8

print(f"My name is {name}, I am {age} years old, and my GPA is {gpa}")

#Conditional Statements
#Age Checker
age = int(input("Enter your age: "))

if age<0:
    print("Invalid age")
elif age>18:
    print("You are an adult")
elif 13<=age<=17:
    print("You are a teenager")
else:
    print("You are a child")

#Even/Odd Checker
num = int(input("Enter a number: "))

if num%2==0:
    print("Even")
else:
    print("Odd")

#Grade Calcu
mark = int(input("Enter marks: "))

if mark<0 or mark>100:
    print("Invalid mark")
elif mark>=90:
    print("A+")
elif mark>=80:
    print("A")
elif mark>=70:
    print("B")
elif mark>=60:
    print("C")
elif mark>=50:
    print("D")
else:
    print("F — Failed")

#Login System
username="admin"
password="1234"
attempts=3

while attempts>0:
    user=input("Enter username: ")
    pwd=input("Enter password: ")

    if user==username and pwd==password:
        print(f"Login successful! Welcome, {user}.")
        break
    elif user==username:
        print("Incorrect password. Try again.")
    else:
        print("User not found.")

    attempts-=1

if attempts==0:
    print("Account locked.")


#ATM Simulation
username="admin"
password="1234"
is_active=True

if not is_active:
    print("Account is disabled.")
else:
    user=input("Username: ")
    pwd=input("Password: ")

    if user==username and pwd==password:
        pinNumber=1111
        balance=10000
        attempts=3

        while attempts>0:
            pin=int(input("Enter ATM PIN: "))

            if pin==pinNumber:
                request=int(input("Enter withdrawal amount: "))

                if request<= 500:
                    print("Minimum withdrawal amount is 500.")
                elif request>balance:
                    print("Insufficient balance.")
                else:
                    balance-=request
                    print("Withdrawal successful.")
                    print("Remaining balance:", balance)
                break
            else:
                attempts-=1
                print(f"Wrong pin. Attempts remaining: {attempts}")

        if attempts==0:
            print("Card blocked!")
    else:
        print("Login failed.")


#BasicLoops
#For loop - for any conditions
for i in range(1, 21):    #10 to 1
    print(i)

for i in range(1, 11):      #Multiplication table of 7
    print(f"7x{i}={7*i}")

total = 0    #Sum of 1 to 100    
for i in range(1, 101):
    total+=i
print(total)

for i in range(2, 51, 2):        #Even numbers 1 to 50
    print(i)

fruits = ['apple', 'banana', 'cherry', 'mango', 'grape']          #Fruits list with position
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

#While LOOP - When condition is true
i = 10         #10 to 1
while i>=1:
    print(i)
    i-=1

total = 0      # Sum until 0 or negative
while True:
    num=int(input("Enter a positive number: "))
    if num<=0:
        break
    total+=num
print("Total:", total)

i=10   #Countdown        
whilei>=0:
    print(i)
    i-=1
print("Blast off!")

count=1     #First 10 multiples of 6
while count<=10:
    print(6*count)
    count+=1

