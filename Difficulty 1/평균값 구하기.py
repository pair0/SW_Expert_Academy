T = int(input())

for test_case in range(1, T+1):
    num_list = list(map(int, input().split()))
    print(f"#{test_case} {round(sum(num_list)/len(num_list))}") # round 반올림 함수