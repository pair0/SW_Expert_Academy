baseAZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
base = {i: ord(i)-65 for i in baseAZ}

for a in baseAZ.lower():
    base[a] = ord(a)-71
for n in range(0, 10):
    base[str(n)] = ord(str(n))+4

base["+"] = 62
base["/"] = 63

T = int(input())
for test_case in range(1, T+1):
    bit = input()
    result = ""
    for j in range(0, len(bit), 4):
        temp = ""
        for k in bit[j:j+4]:
            # 바이너리로 변환후 (6의 배수만큼 왼쪽의 0을 붙여준다.)
            temp += format(base[k], 'b').zfill(6)
        for m in range(0, len(temp), 8):
            result += chr(int(temp[m:m+8], 2))
    print(f"#{test_case} {result}")
