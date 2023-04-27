T = int(input())


def day(m, d, answer):
    if m == m1:
        answer += (d - d1 + 1)
    elif m == m2:
        answer += d2
    else:
        answer += d
    return answer


for test_case in range(1, T+1):
    answer = 0
    m1, d1, m2, d2 = map(int, input().split())

    for m in range(m1, m2+1):
        if m1 == m2:
            answer = d2 - d1 + 1
        elif m in [1, 3, 5, 7, 8, 10, 12]:
            answer = day(m, 31, answer)
        elif m in [4, 6, 9, 11]:
            answer = day(m, 30, answer)
        else:
            answer = day(m, 28, answer)

    print(f"#{test_case} {answer}")
