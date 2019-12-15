#전위순회( (루트) (왼쪽 자식) (오른쪽 자식) )
def preorder(nd):
    print(nd.item,end='')
    if nd.l != ".":
        preorder(tree[nd.l])
    if nd.r != ".":
        preorder(tree[nd.r])
#중위순회( (왼쪽 자식) (루트) (오른쪽 자식) )
def inorder(nd):
    if nd.l != ".":
        inorder(tree[nd.l])
    print(nd.item,end='')
    if nd.r != ".":
        inorder(tree[nd.r])
#후위순회( (왼쪽 자식) (오른쪽 자식) (루트) )
def postorder(nd):
    if nd.l != ".":
        postorder(tree[nd.l])
    if nd.r != ".":
        postorder(tree[nd.r])
    print(nd.item,end='')

class Node:
    def __init__(self,item,l,r):
        self.item = item
        self.l = l
        self.r = r

n = int(input())
tree = {}
for i in range(n):
    data = input().split()
    tree[data[0]] = Node(data[0],data[1],data[2]) #왼쪽 노드 오른쪽 노드
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
