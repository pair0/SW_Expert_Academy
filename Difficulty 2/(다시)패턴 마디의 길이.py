T = int(input())

for test_case in range(1, T+1):
    answer = 0
    s = input()

    for i in range(1, 10):
        if s[:i] == s[i:2*i]:
            answer = i
            break

    print(f"#{test_case} {answer}")
