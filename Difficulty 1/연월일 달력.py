T = int(input())

for test_case in range(1, T+1):
    num = str(input())
    year = num[0:4]
    month = num[4:6]
    day = num[6:8]
    if(int(month) >= 1 and int(month) <= 12):
        if(int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) >= 1 and int(day) <= 31):
            print(f"#{test_case} {year}/{month}/{day}")
        elif(int(month) in [4, 6, 9 , 11] and int(day) >= 1 and int(day) <= 30):
            print(f"#{test_case} {year}/{month}/{day}")
        elif(int(month) == 2 and int(day) >= 1 and int(day) <= 28):
            print(f"#{test_case} {year}/{month}/{day}")
        else:
            print(f"#{test_case} -1")
    else:
        print(f"#{test_case} -1")