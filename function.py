#A function is a reusable block of code

# #1
# def hello():
#     print("hello how are you ")
#     print("what is your name ? ")
# hello()

# #2
# def mohit():
#     print("hello how are you ")
#     print("what is your name ? ")
# mohit()



# a = int(input("enter ypur first number : "))
# b = int(input("enter ypur second number : "))
# def addition():
#     print(a + b )
# addition()


# def addition(a,b):
#     print(a + b)

# addition(25,55)
# addition(27,59)
# addition(255,515)
# addition(255,50589)
# addition(257,578)


# def palindrom_checker(a):
#     copy = a
#     rev = 0

#     while a > 0:
#        rev = rev * 10 + a%10
#        a = a //10

#     if copy == rev:
#         print("number is palindrom")
#     else:
#         print("number is not pallindrom")

# a = int(input("enter your number : "))
# palindrom_checker(a)


# type of argument
# type 1 : Positional argument

def multiplication(a,b,c,d): # 'a', 'b', 'c', and 'd' are the PARAMETERS (the placeholders)
    print(a*b*c*d)

multiplication(5,8,6,9) # 5, 8, 6, and 9 are the ARGUMENTS




def multiplication(a,b,c,d):
    print(f"{5}*{2}*{5}*{2} = {5*2*5*2}")

multiplication(5,2,5,2)





# type 2 : Default argument ka mean hai ki tum apne perameter ki default value likh doge


# def addition(a,b,c = 45):
#     print(a+b+c)

# addition(5,5)



# def subtraction(a,b = 45,c = 45):
#     print((a+b)/c)

# subtraction(0)




# a = str(input("enter your name : "))

# def job(name = a):
#     print(f"hello {name}")

# job()








    
