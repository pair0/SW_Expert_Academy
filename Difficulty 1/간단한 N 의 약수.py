number = int(input())

for i in range(number, 0, -1):
    if (number % i == 0):
        print(number // i, end=" ") #// : 몫 구하기