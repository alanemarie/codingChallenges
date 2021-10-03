## Description:

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root),
which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.

For example, given the following Node class

class Node:
   def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

## My comments:

To serialize into a string, we can use pre, in, or post order (and
the same method we use to serialize, we have to use to desserialize it).

The solution below is based in the one available in
https://gist.github.com/folksilva/91cdbf958b3a496294f525c727676d2f
