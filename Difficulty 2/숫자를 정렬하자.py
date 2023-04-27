T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    number_list = sorted(list(map(int, input().split())))

    print(f"#{test_case}", *number_list)  # *으로 list 출력시 맨 앞에도 띄어쓰기가 있다.
