T = int(input())

for test_case in range(1, T+1):
    answer = 0
    origin_memory = [int(i) for i in input()]
    length = len(origin_memory)
    clean_memory = [0 for _ in range(length)]
    one_first = origin_memory.index(1)

    for i in range(one_first, len(origin_memory)):
        if origin_memory[i] == clean_memory[i]:
            continue
        elif origin_memory[i] == 1:
            clean_memory[i:] = [1 for _ in range(len(clean_memory[i:]))]
        else:
            clean_memory[i:] = [0 for _ in range(len(clean_memory[i:]))]
        print(clean_memory)
        answer += 1

    print(f"#{test_case} {answer}")
