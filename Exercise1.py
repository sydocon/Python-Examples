# Declare a variable and initialize it
f=0
print(f)

#re-declaring the variable works
f="abc"
print(f)

# ERROR: the variable of different types cannot be combined
print("This is a string " + 123)

# This fixes it
print("This is a string " + str(123))

# Global vs. local variables in functions
def someFunc():
  f="def"
  print(f)
  

# prints "def"
someFunc()

# prints "abc"
print(f)

d=1

#prints 1
print(d)

def anotherFunc():
    global d
    d="global"
    print(d)
    
#prints "global"
anotherFunc()

#prints "global"
print(d)

#ERROR: cannot print d because variable is gone
del d
print(d)
