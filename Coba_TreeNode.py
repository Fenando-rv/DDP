class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def print_tree(node, level=0):
    print(' ' * level * 4 + str(node.data))
    for child in node.children:
        print_tree(child, level + 1)

# Contoh Inputan

