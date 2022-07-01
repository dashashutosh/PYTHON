def swap1(num1,num2):

   print('\nInitially: \nValue of num1 is',num1,'\nValue of num2 is',num2)
   num1,num2=num2,num1
   print('\nAfter swapping directly: \nValue of num1 is',num1,'\nValue of num2 is',num2)

def swap2(num1,num2):

   print('\nInitially: \nValue of num1 is',num1,'\nValue of num2 is',num2)
   temp=num1
   num1=num2
   num2=temp
   print('\nAfter swapping using temporary variable: \nValue of num1 is',num1,'\nValue of num2 is',num2)

def swap3(num1,num2):

   print('\nInitially: \nValue of num1 is',num1,'\nValue of num2 is',num2)
   num1=num1+num2
   num2=num1-num2
   num1=num1-num2
   print('\nAfter swapping using arithmetic operator: \nValue of num1 is',num1,'\nValue of num2 is',num2)

def swap4(num1,num2):

   print('\nInitially: \nValue of num1 is',num1,'\nValue of num2 is',num2)
   num1=num1^num2
   num2=num1^num2
   num1=num1^num2
   print('\nAfter swapping using bitwise xor operator: \nValue of num1 is',num1,'\nValue of num2 is',num2)

def main():
	
   num1=int(input('\nEnter 1st no. '))
   num2=int(input('Enter 2nd no. '))
   swap1(num1,num2)

   num1=int(input('\nEnter 1st no. '))
   num2=int(input('Enter 2nd no. '))
   swap2(num1,num2)

   num1=int(input('\nEnter 1st no. '))
   num2=int(input('Enter 2nd no. '))
   swap3(num1,num2)

   num1=int(input('\nEnter 1st no. '))
   num2=int(input('Enter 2nd no. '))
   swap4(num1,num2)

if(__name__=='__main__'):
	main()