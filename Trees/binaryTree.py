import random
import math

class TreeNode:
    def __init__(self,key):
        self.key = key
        self.r = None
        self.l = None
        self.size = 0
        self.depth = 1
    # inserting new key to the tree, the order of adding items is 
    # important cause it determines the balance of your tree
    # so in order to cunstruct a more balanced tree we add 5 million 
    # integer record randomly using random library 
    # the search cost for the tree is of O(log(n))
    def new_key_insert(self,root, new_key):
        if root == None:
            root = TreeNode(new_key)
            return root
        if new_key < root.key:
            root.l = self.new_key_insert(root.l, new_key)
        else:
            root.r = self.new_key_insert(root.r, new_key)
        self.size += 1
        return root
    
    def getMin(self):
        temp = self
        while temp.l:
            temp = temp.l
        return temp.key
    def getMax(self):
        temp = self
        while temp.r:
            temp = temp.r
        return temp.key

    def getsize_(self):
        return self.size

    def print_tree(self):
        print(self.key)
        if self.r:
            self.r.print_tree()
        if self.l:
            self.l.print_tree()

    def getdepth_(self):
        return math.floor(math.log2(self.size))+1


    def getKeyDepth(self,node,key):

        if node.key == key:
            return 1
        elif node.key < key:
            if node.r:
                return self.getKeyDepth(node.r,key)+1
        elif node.key > key:
            if node.l:
                return self.l.getKeyDepth(node.l,key)+1

def getrand_(start,end):
    return math.floor(random.randrange(start,end))

def getsubtree_(root,key):
        m = root.getKeyDepth(root,key)
        print(m)
        min_key = root.getMin()
        sub_root = TreeNode(key)
        l = root.getsize_() 
        d_l =root.getdepth_()
        k = 2 ** (d_l)
        size = l - k
        for i in range(0,size):
            sub_root = sub_root.new_key_insert(sub_root,getrand_(min_key,m.r.key))
        return sub_root

      
r = TreeNode(70)
for i in range(0,150):
    r = r.new_key_insert(r,getrand_(5,150))


print(r.print_tree())