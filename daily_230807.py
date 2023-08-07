

# 1221. 5일차 - GNS

# import sys
# sys.stdin = open('input_1221.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N = list(input().split(' '))
#     my_list = list(input().split(' '))
#
#     for i in range(len(my_list)):
#         if my_list[i] == 'ZRO':
#             my_list[i] = 0
#         elif my_list[i] == 'ONE':
#             my_list[i] = 1
#         elif my_list[i] == 'TWO':
#             my_list[i] = 2
#         elif my_list[i] == 'THR':
#             my_list[i] = 3
#         elif my_list[i] == 'FOR':
#             my_list[i] = 4
#         elif my_list[i] == 'FIV':
#             my_list[i] = 5
#         elif my_list[i] == 'SIX':
#             my_list[i] = 6
#         elif my_list[i] == 'SVN':
#             my_list[i] = 7
#         elif my_list[i] == 'EGT':
#             my_list[i] = 8
#         elif my_list[i] == 'NIN':
#             my_list[i] = 9
#
#     my_list.pop()                               # 맨 마지막에 '' 제거
#     my_list.sort()                              # 리스트 정렬
#
#     for i in range(len(my_list)):
#         if my_list[i] == 0:
#             my_list[i] = 'ZRO'
#         elif my_list[i] == 1:
#             my_list[i] = 'ONE'
#         elif my_list[i] == 2:
#             my_list[i] = 'TWO'
#         elif my_list[i] == 3:
#             my_list[i] = 'THR'
#         elif my_list[i] == 4:
#             my_list[i] = 'FOR'
#         elif my_list[i] == 5:
#             my_list[i] = 'FIV'
#         elif my_list[i] == 6:
#             my_list[i] = 'SIX'
#         elif my_list[i] == 7:
#             my_list[i] = 'SVN'
#         elif my_list[i] == 8:
#             my_list[i] = 'EGT'
#         elif my_list[i] == 9:
#             my_list[i] = 'NIN'
#
#     print(f'#{tc}')
#     print(*my_list)



# 18221. 문자열 비교

# import sys
# sys.stdin = open('input_18221.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N = input()
#     M = input()
#     list_N = list(N)
#     list_M = list(M)
#     num_N = len(list_N)
#     num_M = len(list_M)
#     my_list = []
#     result = 0
#
#     for j in range(num_M - num_N+1):
#         compare = list_M[j:j+num_N]
#         if compare == list_N:
#             result = 1
#
#     print(f'#{tc} {result}')



# 18222. 회문

import sys
sys.stdin = open('input_18222.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(str,input())) for _ in range(N)]
    my_str = ''
    for row in range(N):                        # 가로 파리채
        my_str = ''
        for col in range(N):
            for row2 in range(M):
                if 0 <= row + row2 < N
                    my_str += arr[row + row2][col + col2]

            if my_str[::-1] ==

    print(my_str)


        # 1. m 길이로 다 빼놓고
        # 2. 회문인거 찾기

















# 1989. 초심자의 회문 검사

# import sys
# sys.stdin = open('input_1989.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     my_str = input()
#     num = len(my_str)
#     my_list = list(my_str)
#
#     for i in range(num//2):
#         my_list[i], my_list[num-1-i] = my_list[num-1-i], my_list[i]
#
#     rev_str = ''.join(my_list)
#
#     if rev_str == my_str:
#         result = 1
#     else:
#         result = 0
#
#     print(f'#{tc} {result}')