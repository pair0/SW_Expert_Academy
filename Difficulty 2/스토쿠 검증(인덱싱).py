T = int(input())


def fun():
    for i in range(9):
        # print("1", puzzle[i])
        # print("2", [j[i] for j in puzzle])
        # print("3", sorted(sum([j[(i % 3)*3:(i % 3)*3+3]
        #       for j in puzzle][(i//3)*3:(i//3)*3+3], [])))

        # print("3", puzzle[(i//3)*3:(i//3)*3+3][(i % 3)*3:(i % 3)*3+3])
        if sorted(puzzle[i]) != number_list:
            return 0
        if sorted([j[i] for j in puzzle]) != number_list:
            return 0
        # sum(iterable, start)은 start에 iterable의 모든 데이터를 더하는 함수
        if sorted(sum([j[(i % 3)*3:(i % 3)*3+3] for j in puzzle][(i//3)*3:(i//3)*3+3], [])) != number_list:
            return 0
    return 1


for test_case in range(1, T+1):
    answer = -1  # 겹치는 숫자가 없을 경우 1, 있을 경우 0
    puzzle = list()
    number_list = [i for i in range(1, 10)]

    for i in range(9):
        puzzle.append(list(map(int, input().split())))

    answer = fun()

    print(f"#{test_case} {answer}")
