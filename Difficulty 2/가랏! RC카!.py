T = int(input())

for test_case in range(1, T+1):
    answer = 0
    N = int(input())
    command = list()
    now = 0

    for i in range(N):
        command.append(list(map(int, input().split())))

    for i in range(N):
        if command[i][0] == 1:  # 가속일 때
            now += command[i][1]
        elif command[i][0] == 2:  # 감속일 때
            now -= command[i][1]
            if now < 0:  # 속도가 0보다 작아지면 0으로
                now = 0
        answer += now

    print(f"#{test_case} {answer}")
