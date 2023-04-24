# Counter 사용
from collections import Counter
T = int(input())

for _ in range(T):
    test_case = int(input())
    number = map(int, input().split())
    print(
        f"#{test_case} {sorted(sorted(Counter(number).most_common(), reverse=True), key=lambda x:x[1], reverse=True)[0][0]}")


# Counter 미사용 (이게 더 빠름)
T = int(input())

for _ in range(T):
    test_case = int(input())
    number = map(int, input().split())
    hash_map = dict()

    # 각 인덱스 값 숫자 세기
    for i in number:
        hash_map[i] = hash_map.get(i, 0) + 1

    hash_map = sorted(hash_map.items(), key=lambda x: x[0], reverse=True)
    hash_map = sorted(hash_map, key=lambda x: x[1], reverse=True)
    print(f"#{test_case} {hash_map[0][0]}",)


# # ChatGpt
# T = int(input())  # 테스트 케이스의 수 T 입력

# for i in range(T):
#     test_case = input().split()  # 테스트 케이스 번호와 점수 입력
#     scores = list(map(int, input().split()))  # 점수 리스트로 변환
#     freq = {}  # 빈도수를 저장할 딕셔너리 생성

#     # 각 점수가 몇 번 나타나는지 빈도수 계산
#     for score in scores:
#         freq[score] = freq.get(score, 0) + 1

#     # 빈도수가 가장 높은 점수 중 가장 큰 값을 찾아서 출력
#     mode = max(freq.items(), key=lambda x: (x[1], x[0]))[0]

#     print(f"#{test_case[0]} {mode}")
