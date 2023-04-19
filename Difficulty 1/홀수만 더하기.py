T = int(input())

for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))
    result = 0
    for add in num_list:
        if (add % 2 != 0):
            result += add
    print("#{} {}".format(test_case, result))

