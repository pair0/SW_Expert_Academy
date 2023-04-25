# 1 (이게 더 빠름)
T = int(input())

for test_case in range(1, T+1):
    s = input()
    length = len(s)
    answer = 0

    if length % 2 != 0:  # 길이가 홀수 일 때
        if s[:length//2] == ''.join([s[i] for i in range(len(s)-1, length//2, -1)]):
            answer = 1
    else:  # 길이가 짝수 일 때
        if s[:length//2] == ''.join([s[i] for i in range(len(s)-1, length//2-1, -1)]):
            answer = 1

    print(f"#{test_case} {answer}")


# # 2
# T = int(input())

# for test_case in range(1, T+1):
#     s = input()
#     for i in range(len(s)//2):
#         if s[i] == s[-1-i]:
#             answer = 1
#         else:
#             answer = 0
#     print(f"#{test_case} {answer}")
