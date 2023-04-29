T = int(input())

for test_case in range(1, T+1):
    answer = 0
    # P : A사의 1L당 요금
    # Q : B사의 기본요금
    # R : B사의 초과 요금 기준 (L)
    # S : B사의 1L 당 초과 요금
    # W : 달의 사용하는 수도의 양 (L)
    P, Q, R, S, W = map(int, input().split())

    # A사의 수도 요금
    A = P * W

    # B사의 수도 요금
    if R >= W:
        B = R
    else:
        B = R + (S * (W - R))

    if A <= B:
        answer = A
    else:
        answer = B

    print(f"#{test_case} {answer}")
