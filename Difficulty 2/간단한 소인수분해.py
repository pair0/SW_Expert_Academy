T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    answer = [0] * 5

    while N >= 2:
        if N % 2 == 0:
            answer[0] += 1
            N //= 2
        elif N % 3 == 0:
            answer[1] += 1
            N //= 3
        elif N % 5 == 0:
            answer[2] += 1
            N //= 5
        elif N % 7 == 0:
            answer[3] += 1
            N //= 7
        elif N % 11 == 0:
            answer[4] += 1
            N //= 11

    print(f"#{test_case}", *answer)
