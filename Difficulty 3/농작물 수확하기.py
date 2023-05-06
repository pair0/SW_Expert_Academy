T = int(input())

for test_case in range(1, T+1):
    answer = 0
    N = int(input())
    values = list()

    for i in range(N):
        values.append([int(i) for i in input()])

    for i in range(N):
        if i <= N//2:
            answer += sum(values[i][N//2-i:N//2+i+1])
        else:
            answer += sum(values[i][N//2-(N-i-1):N//2+(N-i-1)+1])

    print(f"#{test_case} {answer}")
