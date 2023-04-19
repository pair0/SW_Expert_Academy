import statistics as st
T = int(input())
num_list = list(map(int, input().split()))
print(st.median(num_list))