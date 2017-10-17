""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def is_BST(node, left, right):
    if node is None:
        return True
    if not left < node.data < right:
        return False
    return is_BST(node.left, left, node.data) and is_BST(node.right, node.data, right)

def checkBST(root):
     return is_BST(root,0,10000)
