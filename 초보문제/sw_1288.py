T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = set()
    count = 0
    while len(nums) < 10:
        count += 1
        nums.update(str(N*count))
    print('#{}'.format(t), N*count)