for test_case in range(1, 10 + 1):
    answer = 0
    t_number = int(input())
    number_list = [list(map(int, input().split())) for _ in range(100)]
    max_number = [0, 0, 0, 0]

    # 각 행의 합 중 최댓값
    for i in range(len(number_list)):
        temp = sum(number_list[i])
        if max_number[0] < temp:
            max_number[0] = temp

        # 각 대각선의 합
        max_number[2] += number_list[i][i]
        max_number[3] += number_list[i][len(number_list) - i - 1]

    # 각 열의 합 중 최댓값
    for j in list(zip(*number_list)):
        temp = sum(j)
        if max_number[1] < temp:
            max_number[1] = temp

    answer = max(max_number)

    print(f"#{test_case} {answer}")
