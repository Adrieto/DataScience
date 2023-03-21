#-------------------------------------------------------------------------------
#                       ESTE PROGRAMA QUEDÓ INCOMPLETO
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
        if self.root != None:                       
            if find_val == self.root.value:
                return True
            else:
                result = self._search(find_val, self.root)
        
        #elif self.root.value != find_val:
        #    self._search(find_val, self.root.left)
        #    return result == find_val
            
        #return False
    
    def _search(self, val, node):
        if val == node.value:
            return True

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
             
        traversal = self.preorder_print(self.root)
        traversal = traversal[:-1] # we get rid of the last "-" in the string
        
        # The output is reformated    
        
        return traversal

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        return False


    def preorder_print(self, start):
        """Helper method - use this to create a recursive print solution."""
        # Start = root 
        
        current_node = start

        if current_node is None:
                        
            return ""
        else:
            lista = ""
            lista += str(current_node.value) + "-"
            lista += str(self.preorder_print(current_node.left))
            lista += str(self.preorder_print(current_node.right))
            
            return lista
        


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


