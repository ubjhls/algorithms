def preorder(node):
    if node.item == '+':
        return preorder(tree[node.lchild]) + preorder(tree[node.rchild])
    elif node.item == '-':
        return preorder(tree[node.lchild]) - preorder(tree[node.rchild])
    elif node.item == '/':
        return preorder(tree[node.lchild]) / preorder(tree[node.rchild])
    elif node.item == '*':
        return preorder(tree[node.lchild]) * preorder(tree[node.rchild])
    else:
        return int(node.item)
class Node:
    def __init__(self, num, item, lchild, rchild):
        self.num = num
        self.item = item
        self.lchild = lchild
        self.rchild = rchild

for t in range(1, 11):
    n = int(input())
    tree = {}
    for j in range(n):
        data = ['0', '0', '0', '0']
        tmp = input().split()
        for k in range(len(tmp)):
            data[k] = tmp[k]
        tree[data[0]] = Node(num=data[0], item=data[1], lchild=data[2], rchild=data[3])
    result = preorder(tree['1'])
    print('#{} {}'.format(t, int(result)))