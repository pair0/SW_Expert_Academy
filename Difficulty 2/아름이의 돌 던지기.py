T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    stone = list(map(int, input().split()))
    stone = sorted(list(map(abs, stone)))

    answer = [stone[0], stone.count(stone[0])]
    print(f"#{test_case}", *answer)
