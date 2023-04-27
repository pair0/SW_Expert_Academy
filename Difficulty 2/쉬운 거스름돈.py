T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    answer = [0, 0, 0, 0, 0, 0, 0, 0]
    count = 0

    for i in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
        answer[count] = N // i
        N = N % i
        count += 1

    print(f"#{test_case}")
    print(*answer)
