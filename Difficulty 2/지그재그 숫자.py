T = int(input())

for test_case in range(1, T+1):
    answer = 0
    N = int(input())

    for i in range(1, N+1):
        if i % 2 != 0:  # 홀수
            answer += i
        else:  # 짝수
            answer -= i
        print(answer)

    print(f"#{test_case} {answer}")
