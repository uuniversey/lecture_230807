

# s = 'Reverse'
# s_lst = list(s)
# N = len(s)
# print(N)


# str 함수를 사용하지 않고 itoa(a)를 구현해본다.

def itoa(a):
    s = ''
    while a>0:
        s += chr(ord('0') + a % 10)   #1의 자리 숫자의 ASCII 값
        a //= 10
    return s[::-1]

a = 123
print(itoa(a))
