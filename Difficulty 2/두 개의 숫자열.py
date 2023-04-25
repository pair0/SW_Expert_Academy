T = int(input())


def mul(index, small, flag):
    value = 0

    for j in range(small):
        if flag == 0:
            value += (A[j+index] * B[j])
        elif flag == 1:
            value += (B[j+index] * A[j])
        else:
            value += (B[j] * A[j])

    return value


for test_case in range(1, T+1):
    answer = 0
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    total = 0

    for i in range(abs(M-N)+1):
        if N > M:
            total = mul(i, M, 0)
        elif M > N:
            total = mul(i, N, 1)
        else:
            answer = mul(i, N, -1)
            break

        if answer < total:
            answer = total

    print(f"#{test_case} {answer}")
