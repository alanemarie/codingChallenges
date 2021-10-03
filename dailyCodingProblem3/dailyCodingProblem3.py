#This problem was asked by Google.

#Given the root to a binary tree, implement serialize(root),
#which serializes the tree into a string, and deserialize(s),
#which deserializes the string back into the tree.

#For example, given the following Node class

#class Node:
#   def __init__(self, val, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right
#The following test should pass:
#
#node = Node('root', Node('left', Node('left.left')), Node('right'))
#assert deserialize(serialize(node)).left.left.val == 'left.left'


#[My comments]:
#To serialize into a string, we can use pre, in, or post order (and
#the same method we use to serialize, we have to use to desserialize it.

#The solution below is based in the one available in
#https://gist.github.com/folksilva/91cdbf958b3a496294f525c727676d2f




class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



######
# - input: s (serialized tree into a string)
# - output: node (tree of type Node)
#
# In-order is used to deserialize the string into a tree.
#
# Complexity: Θ(n)
def deserialize(s):

    #iterator over the nodes written in the string
    sIter = iter(s.split())

    #[in-order traversal]
    #
    #it is implemented inside the function deserialize so we can control
    #the nodes that will be inserted in the tree
    #
    #if the string read in the current position of the iterator is not '-',
    #then we create the node.
    def generateTree():
        nodeName = next(sIter,-1)
        if nodeName != '-':
            node = Node(nodeName)
            node.left = generateTree()
            node.right = generateTree()
            return node
        else:
            return None
    return generateTree()
    
######
# - input: root (structure of type Node)
# - output: s (serialized string)
#
# In-order is used to serialize the tree into a string.
#
# Complexity: Θ(n)
######
def serialize(root):
    l = []

    #[in-order traversal]
    #
    #it is implemented inside the function serialize so we can control
    #the nodes that will be inserted in the string
    #
    #if node is None, then an hyphen is inserted in the string so
    #we can control these type of nodes in the creation of the tree
    #in the desserialized function
    def generateString(node):
        if node != None:
            l.append(str(node.val))
            generateString(node.left)
            generateString(node.right)
        else:
            l.append(str('-'))
    generateString(root)

    #creating the string from the list of read nodes
    s = ''
    for x in l:
        s += x + ' '
    return s
        

def main():
    tree = Node('root',Node('left',Node('left.left')), Node('right'))
    serializedTree = serialize(tree)

    assert deserialize(serializedTree).left.left.val == 'left.left'
    

if __name__ == "__main__":
    main()
