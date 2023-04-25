T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    prof = 0
    max_price = price[-1]

    for test_case2 in range(N - 2, -1, -1):
        if (price[test_case2] < max_price):
            prof += max_price - price[test_case2]
        else:
            max_price = price[test_case2]

    print(f"#{test_case} {prof}")