import math
import random

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
# Compare the new value with the parent node
      if self.data:
         if data <= self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data

# Print the tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()
   def PrintTree2(self):
      if self.right:
         self.right.PrintTree2()
      print(self.data),
      if self.left:
         self.left.PrintTree2()

# Use the insert method to add nodes
root = Node(500)
# root.PrintTree()

for i in range(1,1000):
     a  = math.floor(random.random()*1000) + 1
     root.insert(a)

root.PrintTree()