#Strings & Type Conversion

a = "H"
print(ord(a))


"""
String Indexing

Every character in a string has a position number called an index. 
Positive indexes count from the left (starting at 0), negative from the right (starting at -1)"""

b = "collage"             #72
print("b")                #b
print(b[0])               #c
print(b[3])               #l
print(b[5])               #g
print(b[6] , b[-1] )      #e e


#String Slicing
#string[start : stop : step]--note that stop index is excluded.

x = "STUDENT"
print(x[2:7:1])  #UDENT
print(x[0:5:2])  #SUE
print(x[0:7:3])  #SDT


y = "hello"
print(y[1:4])    # ell  (index 1,2,3 — 4 excluded)
print(y[::-1])   # olleh  (reversed!)

#example

z = "how are you"
#how
print(z[:3:1])

#you
print(z[8:12:1])

#are
print(z[4:7:1])


"""
Type Conversion
You can convert a value from one type to another using these built-in functions
"""

a ="12"
b = int(a)

print(type(a))   #str
print(type(b))   #int



c = "12"
d = float(c)
e = int(c)

print(d)         #12.0
print(e)         #12     

print(type(c))   #str
print(type(d))   #float
print(type(e))   #int




g = 45
h = float(g)
i = str(g)
j = bool(g)

print(h)      
print(i)        
print(j)

print(type(g))   #int
print(type(h))   #float
print(type(i))   #str
print(type(j))   #bool


q = 4587
print(q/2)
print(type(q))

""" The 7 Falsy Values
Everything converts to True with bool() — except these 7 values which become False:

0
0.0
False
""
[]
{}
()
"""