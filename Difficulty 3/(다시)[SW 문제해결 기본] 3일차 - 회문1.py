for test_case in range(1, 1+1):
    answer = 0
    length = int(input())
    s = list()

    if length % 2 == 0:
        flag = 1
    else:
        flag = 0

    for i in range(8):
        s.append([j for j in input()])

    for i in range(8):

        for j in range(8-length+1):
            if s[i][j:(length//2)+j] == [s[i][k] for k in range(length+j-1, (length//2)+j-flag, -1)]:
                answer += 1

        s_wid = [h[i] for h in s]

        for j in range(8-length+1):
            if s_wid[j:(length//2)+j] == [s_wid[k] for k in range(length+j-1, (length//2)+j-flag, -1)]:
                answer += 1

    print(f"#{test_case} {answer}")

# 다른 풀이
for test_case in range(1, 10+1):
    N = int(input())
    List = list(input() for _ in range(8))
    answer = 0

    # 가로 확인
    for y in range(8):
        for x in range(8-N+1):
            A = List[y][x:x+N]
            if A == A[::-1]:  # [::-1] 역순
                answer += 1

    # 세로 확인
    for y in range(8-N+1):
        for x in range(8):
            A = ''
            for z in range(N):
                A += List[y+z][x]
            if A == A[::-1]:
                answer += 1

    print(f"#{test_case} {answer}")
