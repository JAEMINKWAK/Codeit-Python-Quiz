# 자리수 합 리턴
def sum_digit(num): #넘버를 인덱스로 가진 "자릿수합함수"를 를 정의할게.
    total = 0 #토탈이라는 변수는 0으로 정의할게.
    str_num = str(num) #"자릿수합함수"의 인덱스는 '문자열'이야. 이름은 str_num이야.
    for digit in str_num: #str_num 속 문자열 "숫자", 그래서 ex)23이 아니라, 2와 3인 이 '숫자'들을 순서대로 불러오면.
        total += int(digit) #토탈 변수 0에 숫자열로 바꾼 '숫자'를 더할거야. 그래서 2+3이 될거야. 
    return total #반복이 끝나면 토탈을 리턴할 거야.

i = 0 #i는 0이야.
range_1000 = 0 #range_1000도 0이야.
while i <= 1000: #i가 1000보다 작거나 같을 동안
    range_1000 += sum_digit(i) #range_1000에 "자릿수합함수"값을 더할거야.
    i += 1 #그 다음 i 에 1을 더하자.

print(range_1000) 
#range_1000를 프린트해보자. 
#1이면 while 가 참이므로, range_1000인 0에 sum_digit(1)의 값인 1인 더해져서 1가 돼.
#2는 윗줄로 1이 된 range_1000에 sum_digit(2)의 값인 2를 더해서 3가 돼.
#3은 윗줄로 3이된 range_1000에 sum_digit(3)의 값인 3를 더해서 6가 돼.
#.... 11은 윗줄로 46이 된 range_1000에 sum_digit(11)의 값인 2를 더해서 48이 돼.
#결국 13501이 나와.