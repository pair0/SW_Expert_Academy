number = input()

for length in range(0, len(number)):
    if(ord(number[length]) >= 97 and ord(number[length]) <= 122): # ord() 숫자를 아스키로 변환
        print(ord(number[length]) - 96, end=" ")
    elif(ord(number[length]) >=65 and ord(number[length]) <= 90):
        print(ord(number[length]) - 64, end=" ")