T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    number_list = list()

    max = -1

    for i in range(N):
        number_list.append(list(map(int, input().split())))

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_list = 0
            for k in range(M):
                sum_list += sum(number_list[i+k][j:j+M])
            if sum_list > max:
                max = sum_list

    print(f"#{test_case} {max}")
