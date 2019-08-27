# testcase = int(input())
# ziphap=[]
# for i in range(1,13,1):
#     ziphap.append(i)
# n = len(ziphap)
#
# for p in range(testcase):
#     test = list(map(int, input().split()))
#     result=[]
#     count = 0
#     for i in range(1<<n):
#         tmp = []
#         for j in range(n):
#             if i & (1<<j):
#                 tmp.append(ziphap[j])
#         result.append(tmp)
#     for k in range(2**12):
#         if len(result[k]) == test[0]:
#             if sum(result[k]) == test[1]:
#                 count += 1
#     print('#{} {}'.format(p+1,count))
