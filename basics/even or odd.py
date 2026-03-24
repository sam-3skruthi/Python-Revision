#even or odd number
num = int(input("Enter the number:"))
print(num)

if (num % 2 == 0):
       print("the number is even!")
else:
       print("the number is odd!")


#checking even or odd for numbers 0-10
for i in range(0,10):
   if (i % 2 == 0):
       print("the number is even!")
   else:
       print("the number is odd!")