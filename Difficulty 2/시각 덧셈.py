T = int(input())

for test_case in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    times = [0, 0]

    times[1] = m1 + m2
    times[0] = h1 + h2

    if times[1] >= 60:
        times[0] += 1
        times[1] -= 60
    if times[0] > 12:
        times[0] -= 12

    print(f"#{test_case}", *times)
