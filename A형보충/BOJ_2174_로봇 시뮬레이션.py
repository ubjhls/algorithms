def is_in(x, y):
    global a, b
    return True if 1<=x<=a and 1<=y<=b else False


a, b = map(int, input().split())
n, m = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
tmp = {"E": 0, "S": 1, "W": 2, "N": 3}
location = []
robot = {}
for i in range(n):
    x, y, d = input().split()
    location.append((int(x), int(y)))
    robot.update({(int(x), int(y)): (tmp[d], i+1)})
flag = True
for _ in range(m):
    r, cmd, times = input().split()
    r, times = int(r)-1, int(times)
    x, y = location[r]
    d, idx = robot.pop((x, y))
    if cmd == "F":
        while times:
            times -= 1
            x, y = x + dx[d], y + dy[d]
            if is_in(x, y):
                try:
                    _, idx2 = robot[(x, y)]
                    flag = False
                    print('Robot {} crashes into robot {}'.format(idx, idx2))
                    break
                except KeyError: continue
            else:
                flag = False
                print('Robot {} crashes into the wall'.format(idx))
                break
        if flag:
            location[r] = (x, y)
            robot.update({(x, y):(d, idx)})
        else:
            break
    elif cmd == "R":
        d = (d + times) % 4
        location[r] = (x, y)
        robot.update({(x, y):(d, idx)})
    else:
        d = (d - times) % 4
        location[r] = (x, y)
        robot.update({(x, y):(d, idx)})
if flag:
    print('OK')