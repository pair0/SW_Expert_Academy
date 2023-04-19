def digit_length(num):
    count = 0
    while num:
        num //= 10
        count +=1
    return count

num = int(input())
n_sum = 0;

for i in (10 ** x for x in range(digit_length(num)-1, -1, -1)):
    n_sum += num//i
    num %=i

print(n_sum)