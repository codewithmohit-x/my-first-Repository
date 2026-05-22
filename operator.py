#Arithmetic Operators

"""
Operator	Name	         Example	 Result
+	      Addition	          10 + 3	  13
-	      Subtraction	      10 - 3	  7
*	      Multiplication	  10 * 3	  30
/	      Division	10 / 3	  3.333…  
//	      Floor Division	  10 // 3	  3
%	      Modulus(remainder)  10 % 3	  1
**	      Exponentiation	  2 ** 8	  256 """



a = 25
b = 15

print(a+b)   
print(a-b)
print(a*b)
print(a/b)     #1.666666667
print(a//b)    #1
print(a%b)
print(a**b)

#Comparison Operators
"""
Operator	Meaning	          Example	  Result
==	         Equal to	        5 == 5	    True
!=	         Not equal to	    5 != 3	    True
>	         Greater than	    5 > 3	    True
<	         Less than	        5 < 3	    False
>=	         Greater or equal	5 >= 5	    True
<=	         Less or equal	    3 <= 5	    True
"""

a = 60
b = 55
print(a==b)
print(a!=b)   
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)



#Logical Operators

'''
Operator               Returns True when…	                   Example
  and	       Both conditions are True	                 age > 18 and has_id == True
  or	       At least one condition is True        	is_admin or is_staff
not	           Reverses the boolean	                    not is_banned
'''

print(12>10 and 14==14 and 58==58)
#all true =========== true
print(12>10 and 14==14 and 58==78)
#(3)2 true, 1 false ================ false

print(52==53 or 95>56 or 58>20)
#ek bhi true tho all true
print(52==53 or 95>506 or 58>20)
#ek bhi true tho all true

print(not 25==25)      #false
print(not 25>85)       #true



#Assignment Operators
"""
Operator	Meaning	                 Equivalent to
+=	          Add and assign	         x = x + n
-=	          Subtract and assign	     x = x - n
*=	          Multiply and assign	     x = x * n
/=	          Divide and assign	         x = x / n
//=	          Floor divide and assign	 x = x // n
%=	          Modulus and assign	     x = x % n
**=	          Power and assign	         x = x ** n
"""

a = 10
a += 10
a += 10
a += 10

print(a)




a = 10
a -= 1
a -= 1
a -= 1

print(a)




a = 10
a *= 2
a *= 2
a *= 2

print(a)






a = 10
a /= 2
a /= 2
a /= 2

print(a)







a = 10
a //= 2
a //= 2
a //= 2

print(a)


