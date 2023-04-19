# for tc in range(1,int(input())+1):
#     data, K = input().split() # 숫자판의 정보, 교환횟수
#     K = int(K)
#     N = len(data)
#     now = set([data])
#     nxt = set()
#     for _ in range(K):
#         while now:
#             s = now.pop()
#             s = list(s)
#             for i in range(N):
#                 for j in range(i+1,N):
#                     s[i],s[j] = s[j],s[i]
#                     nxt.add(''.join(s))
#                     s[i], s[j] = s[j], s[i]
#         now,nxt = nxt,now
#
#     print('#{} {}'.format(tc,max(map(int,now))))


# def dfs_recursive(graph, start, change, visited=[]):
#     ## 데이터를 추가하는 명령어 / 재귀가 이루어짐
#     visited.append(start)
#
#     for node in graph[start]:
#         if node not in visited:
#             dfs_recursive(graph, node, visited)
#     return visited
#
# N = int(input())
#
# for test_case in range(1, N+1):
#     box, change = input().split()
#     box=list(map(int, box))
#     change=int(change)
#
#     result = dfs_recursive(box, 0, change)
#
#
#     print(f"#{test_case} {result}")


# D3 1244 최대상금

# 경우의 수 찾기, 매개변수로 몇번 바꿧는지 적는다.
def dfs(count):
    global answer
    # 횟수를 다 사용했다면
    if not count:
        # 숫자로 바꿔보고
        temp = int(''.join(values))
        # 가지고 있는 최대수보다 크다면 갱신
        if answer < temp:
            answer = temp
        return
    # 바꿔야 하니까 이중 포문
    for i in range(length):
        # 경우의 수를 찾는거니까 i보다 큰위치부터
        for j in range(i + 1, length):
            # 두개의 위치를 바꾸고 나서
            values[i], values[j] = values[j], values[i]
            # 가지치기 해야하니까 일단 합쳐보고
            temp_key = ''.join(values)
            # 어떤수가 몇회차에 나왔는지 체크 1이면 안나온거니까 경우의수에 넣어주기
            if visited.get((temp_key, count - 1), 1):
                # 이숫자는 몇회차에 사용했으니까 체크해주고
                visited[(temp_key, count - 1)] = 0
                # dfs도 돌려주고
                dfs(count - 1)
            # 다 썻으면 원상복귀
            values[i], values[j] = values[j], values[i]


for t in range(int(input())):
    answer = -1
    value, change = input().split()
    # 바꾸기 편하려고 리스트화시킴
    values = list(value)
    change = int(change)
    # 계속 쓸꺼니까 캐스팅
    length = len(values)
    # 가지치기용 딕셔너리
    visited = {}
    dfs(change)
    print('#{} {}'.format(t + 1, answer))