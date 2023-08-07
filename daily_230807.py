

# 1221. 5일차 - GNS

import sys
sys.stdin = open('input_1221.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = list(input().split(' '))
    my_list = list(input().split(' '))




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

# import sys
# sys.stdin = open('input_18222.txt','r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int,input().split())
#     arr = [list(map(str,input())) for _ in range(N)]
#     my_str = ''
#     result = []
#
#     for row in range(N):                        # 가로 파리채
#         for col in range(N):
#             my_str = ''
#             for row2 in range(M):
#                 if 0 <= row + row2 < N:
#                     my_str += arr[row + row2][col]
#                     if len(my_str) == M and my_str[::-1] == my_str:
#                         result.append(my_str)
#
#     for col in range(N):                        # 세로 파리채
#         for row in range(N):
#             my_str = ''
#             for col2 in range(M):
#                 if 0 <= col + col2 < N:
#                     my_str += arr[row][col + col2]
#                     if len(my_str) == M and my_str[::-1] == my_str:
#                         result.append(my_str)
#
#     print(f'#{tc}', *result)



















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