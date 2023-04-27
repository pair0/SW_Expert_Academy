T = int(input())

for test_case in range(1, T+1):
    answer = 0
    N = int(input())
    number_list = set()

    # set에 list()는 add가 안됨
    # set과 list는 비교할 수 있다.
    while sorted(number_list) != [str(i) for i in range(10)]:
        N_mul = N * (answer + 1)
        for i in str(N_mul):
            number_list.add(i)
        answer += 1

    print(f"#{test_case} {N * answer}")
