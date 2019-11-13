testcase = int(input())
dx = [1, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1]

def func(maze,num):
    visit = [[0] * num for _ in range(num)]
    for j in range(num):
        for k in range(num):
            if maze[j][k] == 3:
                stack = [(j,k)]
                break
    while stack:
        x, y = stack.pop()
        for idx in range(5):
            del_x, del_y = x + dx[idx], y + dy[idx]
            if del_y == num:
                del_y = del_y - 1
                continue
            elif del_x == 0:
                del_x = del_x + 1
                continue
            elif del_x == num:
                del_x = del_x - 1
                continue
            elif maze[del_y][del_x] == 2:
                return 1
            elif not maze[del_y][del_x] and not visit[del_y][del_x]:
                stack.append((del_x, del_y))
                visit[del_y][del_x] = 1
                break
    return 0
for i in range(testcase):
    num = int(input())
    maze = [[] for _ in range(num)]
    for j in range(num):
        tmp = input()
        for k in range(num):
            maze[j].append(int(tmp[k]))
    print('#{} {}'.format(i+1,func(maze,num)))