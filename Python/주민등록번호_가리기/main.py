
def mask_security_number(security_number):
    # 코드를 입력하세요.
    num_list = list(security_number)
    num_list_str = ""

    for n in range(0 - len(security_number), 0):
        if -4 <= n <= 0:
            num_list[n] = "*"

        num_list_str += num_list[n]

    return num_list_str

# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))