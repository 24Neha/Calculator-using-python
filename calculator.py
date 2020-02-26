

def add(x,y):
	print("Result is: ",x+y,'\n')
def sub(x,y):
	print("Result is: ",x-y,'\n')
def mul(x,y):
        print("Result is: ",x*y,'\n')
def div(x,y):
        print("Result is: ",x/y,'\n')



while True:
		
		
	a = float(input("Enter first number = "))
	b = float(input("Enter second number = "))
	print("""1. for Additio\n2. for Subtraction\n3. for Multiplication\n4. for Division""")
	s = int(input("Press a valid button: "))
	if   s ==1:
		add(a,b)
	elif s == 2:
      		 sub(a,b)
	elif s == 3:
      		mul(a,b)
	elif s == 4:
  	   	  div(a,b)	
	else:
		print("Invalid button")
	



