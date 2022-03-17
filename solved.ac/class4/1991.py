import sys

n = int(sys.stdin.readline())
tree = {}
for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a] = {}
    tree[a]['l'] = b
    tree[a]['r'] = c

preorder = ""
inorder = ""
postorder = ""


def doPreorder(node):
    preorder += node
    if tree[node]['l'] != '.':
        doPreorder(tree[node]['l'])
    if tree[node]['r'] != '.':
        doPreorder(tree[node]['r'])


def doInorder(node):
    if tree[node]['l'] != '.':
        doInorder(tree[node]['l'])
    inorder += node
    if tree[node]['r'] != '.':
        doInorder(tree[node]['r'])


def doPostorder(node):
    if tree[node]['l'] != '.':
        doPostorder(tree[node]['l'])
    if tree[node]['r'] != '.':
        doPostorder(tree[node]['r'])
    postorder += node


doPreorder('A')
doInorder('A')
doPostorder('A')

print(preorder)
print(inorder)
print(postorder)
