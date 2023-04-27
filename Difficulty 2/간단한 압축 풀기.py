T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    answer = ''
    case_list = list()

    for i in range(N):
        case_list.append(input().split())

    for i in range(N):
        answer += (case_list[i][0] * int(case_list[i][1]))

    print(f"#{test_case}")
    for i in range(len(answer)):
        print(answer[i], end='')
        if (i + 1) % 10 == 0:
            print()
    print()
