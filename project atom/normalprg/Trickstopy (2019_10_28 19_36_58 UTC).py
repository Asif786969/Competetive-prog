#TO ADJUST THE NO OF DECIMAL VALUES
use print("{0:.2f}".format(a)) where a is a floating point no.
============================================================================
============================================================================
#SLICING IN ARRAYS
1)))suppose L is an ARRAY
new sliced array will be S=L[start:end]
here if end is 10 then array will be sliced upto index no 9
2)))all the elements of the array could be printed using *a
============================================================================
============================================================================
#ERRORS
"try" and "except" are the two keywords that are use to define this
try:
    a=10
    b=0
    c=a/b
    print(c)
except :
    print("the values entered must be integers")
The above code will print the value entered incorrectly ,here the except funct and
run on all types of error if not mentioned specifically
for example if we write "except ValueError" then the print function only will work for ValueError
hence then the above output will show zero division error
Also we can put it in while True loop so that user will have to enter the acceptable value for
program
2+++ also the one try can have multiple except
we can also write multiple error in single line as "except(ValueError,ZeroDivisionError):"
===========
class zerodenomerror(Exception):
    pass
try:
    a=10
    b=0
    if(b==0):
        raise zerodenomerror()
    c=a/b
except ZeroDivisionError:
    print("zero")
except zerodenomerror:
    print("the class error")
The order of the func is try==>except==>else==>finally
here if there is no error then the else part will be executed
but the finally will be executed whether error is raised or not
============================================================================================
============================================================================================
from sys import setrecursionlimit
setrecursionlimit(30000)
===========================================================
