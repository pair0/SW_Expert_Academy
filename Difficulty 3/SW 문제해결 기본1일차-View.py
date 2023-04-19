for test_case in range(1, 11):
    building_number = int(input())
    height = list(map(int, input().split()))
    result = 0
    for i in range(2, building_number-2):
        between_building = [height[i-2], height[i-1], height[i+1], height[i+2]]
        if height[i] > max(between_building):
            result += height[i] - max(between_building)
    print(f"#{test_case} {result}")