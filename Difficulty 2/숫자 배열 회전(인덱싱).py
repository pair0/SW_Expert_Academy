T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    N_list = list()
    list_90 = list()
    list_180 = list()
    list_270 = list()

    for i in range(N):
        N_list.append(list(map(int, input().split())))

    for i in range(N):
        # 90도 회전 저장
        list_90.append([str(N_list[j][i]) for j in range(N-1, -1, -1)])
        # 180도 회전 저장
        list_180.append([str(N_list[N-i-1][j]) for j in range(N-1, -1, -1)])
        # 270도 회전 저장
        list_270.append([str(N_list[j][N-i-1]) for j in range(N)])

    print(f"#{test_case}")
    for i in range(N):
        print(''.join(list_90[i]), end=" ")
        print(''.join(list_180[i]), end=" ")
        print(''.join(list_270[i]))
