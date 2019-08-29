length = int(input())
red = list(map(int, input().split()))
blue = list(map(int, input().split()))
yellow = list(map(int, input().split()))

tmp = []
a = (red[0] + red[1])/2
tmp.append(a)
if a < length:
    length = length - a
else:
    length = a
b = (blue[0] + blue[1])/2