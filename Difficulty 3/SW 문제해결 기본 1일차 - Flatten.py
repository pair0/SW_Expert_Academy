for test_case in range(1, 10+1):
    dump_count = int(input())
    box_height = list(map(int, input().split()))
    for i in range(dump_count):
        box_height[box_height.index(max(box_height))] -= 1
        box_height[box_height.index(min(box_height))] += 1
    print(f"#{test_case} {max(box_height) - min(box_height)}")