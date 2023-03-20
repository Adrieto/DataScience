#-------------------------------------------------------------------------------
#  ESTE PROGRAMA QUEDÓ INCOMPLETO
#-------------------------------------------------------------------------------

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        traversal = ""
        self.preorder_print(self.root, traversal)
        
        
        return traversal

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a recursive print solution."""
        # Start = root , traversal = "pre-order"
        
        current_node = start
        aux_list = []

        if current_node is None:
            #print(traversal)
            return traversal
        else:
            #traversal = traversal + str(current_node.value) + "-" 
            self.preorder_print(current_node.left, traversal)
            if not current_node.left in aux_list:
                aux_list.append(current_node.left)
                #traversal = "-".join(aux_list)
            self.preorder_print(current_node.right, traversal)
            if not current_node.left in aux_list:
                aux_list.append(current_node.right)

                #traversal = "-".join(aux_list)
        return aux_list







# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)


# Test search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print (tree.print_tree())


