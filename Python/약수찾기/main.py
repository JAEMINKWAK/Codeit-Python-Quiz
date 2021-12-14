N = 120
i = 1
count = 0

while i <= 120:
    if 120 % i == 0:
        print(i)
        count += 1
    i += 1

print(f"{N}의 약수는 총 {count}개입니다.")