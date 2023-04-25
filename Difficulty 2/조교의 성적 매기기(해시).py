T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    score = list()
    hash_map = dict()
    score_list = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

    # 점수 입력
    for _ in range(N):
        score.append(list(map(int, input().split())))

    # 학생 번호와 점수 매치
    for i in range(N):
        hash_map[i+1] = (score[i][0] * 0.35 + score[i]
                         [1] * 0.45 + score[i][2] * 0.2)

    # 점수 별로 줄세우기
    hash_map = dict(sorted(hash_map.items(), key=lambda x: x[1], reverse=True))

    # 점수 별로 학점주기
    for index, key in enumerate(hash_map.keys()):
        hash_map[key] = score_list[index//(N // 10)]

    print(f"#{test_case} {hash_map[K]}")
