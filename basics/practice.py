print("hello setup is successful!!")
print("yeahhh!! finally")

#variables & data types
a = 30
print(a)
b = 2.5
name = "sam"
print(b)
print(type(b))
print(name)

#conditional statements 
num = int(input("Enter a number:"))

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

#loops
#for loop
for i in range(10):
    print(i)

#while loop
i=1
while i<=6:
    print(i)
    i+=1

#functions
def add(a,b):
    return a+b

print(add(5,3))



