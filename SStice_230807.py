

# s = 'Reverse'
# s_lst = list(s)
# N = len(s)
# print(N)


# str 함수를 사용하지 않고 itoa(a)를 구현해본다.

# def itoa(a):
#     s = ''
#     while a>0:
#         s += chr(ord('0') + a % 10)   #1의 자리 숫자의 ASCII 값
#         a //= 10
#     return s[::-1]
#
# a = 123
# print(itoa(a))



# 직사각형 네개의 합집합의 면적 구하기
# 각 상황 마다의 넓이를 구하고 겹치는 장소는 몇번 겹치는지 확인한 후 겹치는 숫자 만큼 빼줌

# box = [[0] * 100 for _ in range(100)]                   # 최대 범위의 빈 박스 생성
# area = 0                                                # 넓이 초기값
# for i in range(4):                                      # 인풋을 4번 나눠 받음
#     a, b, c, d = map(int,input().split())
#     area += (c-a) * (d-b)                               # 각 상황 마다의 넓이
#     for row in range(a, c):                             # 인풋 받은 정수를 바탕으로 박스마다 1을 채움
#         for col in range(b, d):
#             box[row][col] += 1
#
# overlab = 0                                             # 겹치는 곳의 초기값
#
# for row in range(100):
#     for col in range(100):
#         if box[row][col] >= 2:                          # 겹쳐 있다는 것은 박스에 숫자가 2이상이라는 뜻
#             overlab += box[row][col] - 1                # 겹쳐 있는 숫자만큼 빼줌(1이 남을 때까지 )
#
# result = area - overlab                                 # 전체 넓이의 합에 겹쳐있는 만큼 빼면 답
#
# print(result)