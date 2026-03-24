#armstrong number
#ex : 153 → 1³ + 5³ + 3³ = 153

num = int(input("Enter number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print("Armstrong")
else:
    print("Not Armstrong")