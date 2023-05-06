def dfs(idx):
    if idx == N:
        global answer
        answer += 1
        return

    for i in range(N):
        # 이미 사용한 열이라면 패스
        if visited[i]:
            continue
        # 대각선이 겹친다면 패스
        if possible(idx, i):
            continue
        visited[i] = True
        map_list[idx] = i
        dfs(idx + 1)
        visited[i] = False


def possible(idx, c):
    for i in range(idx):
        if idx - i == abs(c - map_list[i]):
            return True
    return False


T = int(input())
for test_case in range(1, T+1):
    answer = 0
    N = int(input())
    map_list = [False for _ in range(N)]
    visited = [False for _ in range(N)]
    dfs(0)

    print(f"#{test_case} {answer}")
