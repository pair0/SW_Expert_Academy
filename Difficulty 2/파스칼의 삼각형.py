T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    number_list = list()

    for i in range(N):
        number_list.append([1 for _ in range(i+1)])

    for i in range(2, N):
        for j in range(1, i):
            number_list[i][j] = sum(number_list[i-1][j-1:j+1])

    print(f"#{test_case}")
    for i in number_list:
        print(*i)
