def find_pair(root, sum, found):

    if root is None:
        return False

    if find_pair(root.left, sum, found):
        return True

    complement = sum - root.data
    if complement in found:
        print("Pair found:", root.data, ",", complement)
        return True

    found.add(root.data)
    return find_pair(root.right, sum, found)

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):

    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

# Sample input 
root = None
root = insert(root, 10)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 50)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 30)

sum = 130
found = set()
find_pair(root, sum, found)
