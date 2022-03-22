import sys
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline())
inOrder = sys.stdin.readline().split()
postOrder = sys.stdin.readline().split()
tree = {}
originRoot = postOrder[-1]
pos = {}
for i in range(0, n):
    pos[inOrder[i]] = i


def cuttingTree(inStart, inEnd, postStart, postEnd):
    root = postOrder[postEnd - 1]
    tree[root] = {}
    if inEnd - 1 > inStart:
        leftInEnd = pos[root]
        leftPostEnd = postStart + leftInEnd - inStart
        if leftInEnd > inStart:
            tree[root]['l'] = postOrder[leftPostEnd - 1]
            cuttingTree(inStart, leftInEnd, postStart, leftPostEnd)
        if leftInEnd < inEnd - 1:
            tree[root]['r'] = postOrder[postEnd - 2]
            cuttingTree(leftInEnd + 1, inEnd, leftPostEnd, postEnd - 1)


def preorder(r):
    print(r, end=" ")
    if 'l' in tree[r]:
        preorder(tree[r]['l'])
    if 'r' in tree[r]:
        preorder(tree[r]['r'])


cuttingTree(0, n, 0, n)
preorder(originRoot)
print("")
