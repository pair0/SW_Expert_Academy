T = int(input())

for test_case in range(1, T+1):
    answer = 0
    N, K = map(int, input().split())
    puzzle = list()

    for i in range(N):
        puzzle.append(list(map(int, input().split())))

    for i in range(N):
        count_width = 0
        count_hi = 0
        # 가로에 들어갈 수 있는 경우
        for j in range(N):
            if puzzle[i][j] == 1:
                count_width += 1
            else:
                if count_width == K:
                    answer += 1
                count_width = 0

        # 세로에 들어갈 수 있는 경우
        for h in [j[i] for j in puzzle]:
            if h == 1:
                count_hi += 1
            else:
                if count_hi == K:
                    answer += 1
                count_hi = 0

        if count_width == K:
            answer += 1
        if count_hi == K:
            answer += 1

    print(f"#{test_case} {answer}")
