N = int(input("Enter N: "))

numbers = []

for i in range(N):
    number = int(input("Enter number: "))
    numbers.append(number)

X = int(input("Enter X: "))

if X in numbers:
    print(numbers.index(X) + 1)
else:
    print(-1)