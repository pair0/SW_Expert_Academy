T = int(input())


def dfs(index, sTaste=0, sKcal=0):
    global answer
    # 칼로리 넘어가면 리턴
    if sKcal > L:
        return
    # 최고 맛점수보다 높으면 갱시
    if answer < sTaste:
        answer = sTaste
    # 마지막 인덱스까지 내려왔으면 리턴
    if index == N:
        return

    Taste, Kcal = T_KList[index]
    # 재료를 사용했을 때
    dfs(index + 1, sTaste + Taste, sKcal + Kcal)
    # 재료를 사용하지 않았을 때
    dfs(index + 1, sTaste, sKcal)


for test_case in range(1, T + 1):
    answer = 0
    ### N : 재료의 수, L : 제한 칼로리
    N, L = map(int, input().split())
    ### T : 재료에 대한 민기의 맛에 대한 점수, K : 칼로리
    T_KList = [list(map(int, input().split())) for _ in range(N)]
    dfs(0)

    print(f"#{test_case} {answer}")
