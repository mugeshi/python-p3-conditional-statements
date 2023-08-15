#!/usr/bin/env python3

def admin_login(username, password):
    if username == "admin" and password == "password"
       return "Login successful"
    else:
        return "login failed"

print(admin.login("admin", "password"))#output: Login successful
print(admin.login("user", "pass")) #output: login failed


def hows_the_weather(temperature):
   if temperature > 30:
      return "It's hot outside"
    elif temperature >20:
        return "It's a bit pleasant"
    elif temperature > 10:
        return "it's a bit chilly."
    else:
        return "It's cold out there!"
 #Example usage 
 print(hows_the_weather(25))# output: The weather is pleasant
 print(hows_the_weather(5))  # output: It's cold out there!     


    

def fizzbuzz(num):
    if num %  3 == 0 and  num 5 == 0:
         return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return  "Buzz"
    else:
        return str(num)
# Example usage 
for i in range(1, 16):
    print(fizzbuzz(i))

def calculator(operation, num1, num2):
    if operation == "+"
       return num1 + num2
    elif operation == "-":
         return num1-num2
    elif operation == "*":
         return num1*num2:
    elif operation== "/":
        if num2 != 0:
          return num1 / num2
        else:
            return "cannot divide by zero."
    else: 
        return"Invalid operation."
print(calculator("+", 10,5)) # output: 15
print(calculator("/", 10,2)) #output: 5.0
print(calculator("*", 7,3)) # ouptut: 21
print(calculator("-", 8,3)) #output:5 
print(calculator("/", 10,0))#output: cannot divide by zero