T = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for test_case in range(1, T+1):
    N = int(input())
    answer = [[0]*N for _ in range(N)]
    x, y = 0, 0
    dist = 0  # 우:0, 하:1, 좌:2, 상:3

    for i in range(1, N*N+1):
        answer[y][x] = i

        x += dx[dist]
        y += dy[dist]

        if x < 0 or y < 0 or x >= N or y >= N or answer[y][x] != 0:
            x -= dx[dist]
            y -= dy[dist]
            dist = (dist+1) % 4
            x += dx[dist]
            y += dy[dist]

    print(f"#{test_case}")
    for row in answer:
        print(*row)
