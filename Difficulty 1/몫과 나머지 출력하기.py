T = int(input())

for test_case in range(1, 1+T):
    a, b = map(int, input().split())
    print(f"#{test_case} {a//b} {a%b}")