def inorder(node):
    if node.lchild != '0':
        inorder(tree[node.lchild])

    print(node.item, end='')

    if node.rchild != '0':
        inorder(tree[node.rchild])

class Node:
    def __init__(self, num, item, lchild, rchild):
        self.num = num
        self.item = item
        self.lchild = lchild
        self.rchild = rchild

for t in range(1,11):
    n = int(input())
    tree = {}
    for j in range(n):
        data = ['0', '0', '0', '0']
        tmp = input().split()
        for k in range(len(tmp)):
            data[k] = tmp[k]
        tree[data[0]] = Node(num=data[0], item=data[1], lchild=data[2], rchild=data[3])

    print('#{}'.format(t), end = ' ')
    inorder(tree['1'])
    print()
