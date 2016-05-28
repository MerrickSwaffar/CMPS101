#this file contains a python implementation of a red/black tree.
#some of the code in this assignment is based on psuedo code
#from CLRS introduction to algorithms.

#enumeration for node colors
BLACK = 0 
RED = 1

#definition of nil node
class NIL(object):
    def __init__(self):
        self.color = BLACK

nil = NIL()

#Node class for red/black tree 
class Node(object):      
    #Node constructor
    def __init__(self, key, value = 1, p = nil, left = nil, right = nil):
        self.p = p
        self.left = left
        self.right = right
        self.key = key
        self.value = value
        self.color = RED
            
#Python implementation of a red/black tree
class BSTree(object): 
    #BSTree constructor
    def __init__(self):
        self.size = 0
        self.root = nil
    
    #perform a left rotation of the given node
    def rotateleft(self, node):
        if node.right == nil:
            return
        r = node.right
        node.right = r.left
        if r.left != nil:
            r.left.p = node
        r.p = node.p
        if node.p == nil:
            self.root = r
        elif node == node.p.left:
            node.p.left = r
        else:
            node.p.right = r
        r.left = node
        node.p = r 
    
    #perform a right rotation of the given node    
    def rotateright(self, node):
        if node.left == nil:
            return
        l = node.left
        node.left = l.right
        if l.right != nil:
            l.right.p = node
        l.p = node.p
        if node.p == nil:
            self.root = l
        elif node == node.p.right:
            node.p.right = l
        else:
            node.p.left = l
        l.right = node
        node.p = l
    
    #restore the red/black properties to the tree    
    def balance(self, node):
        node.color = RED
        while node != self.root and node.p.color == RED:
            if node.p == node.p.p.left:
                r = node.p.p.right
                if r.color == RED:
                    node.p.color = BLACK
                    r.color = BLACK
                    node.p.p.color = RED
                    node = node.p.p
                else:
                    if node == node.p.right:
                        node = node.p
                        self.rotateleft(node)
                    node.p.color = BLACK
                    node.p.p.color = RED
                    self.rotateright(node.p.p)
            else:
                l = node.p.p.left
                if l.color == RED:
                    node.p.color = BLACK
                    l.color = BLACK
                    node.p.p.color = RED
                    node = node.p.p
                else:
                    if node == node.p.left:
                        node = node.p
                        self.rotateright(node)
                    node.p.color = BLACK
                    node.p.p.color = RED
                    self.rotateleft(node.p.p)
        self.root.color = BLACK
        
    #insert a node with the given key and value into the tree, then balance 
    #the tree.
    def insert(self, key, value = 1):
        node = self.root
        if node == nil:
            self.size += 1
            self.root = Node(key, value)
            return
        while node != nil:
            if node.key == key:
                node.value += value
                return
            elif node.key > key:
                if node.left != nil:
                    node = node.left
                else:
                    self.size += 1
                    node.left = Node(key, value, node)
                    break
            else:
                if node.right != nil:
                    node = node.right
                else:
                    self.size += 1
                    node.right = Node(key, value, node)
                    break
        self.balance(node)
            
    #search for the given key in the tree. return that node if found. 
    def find(self, key, node = None):
        if node == None:
            node = self.root
        while node != nil and key != node.key:
            if node.key > key:
                node = node.left
            else:
                node = node.right
        if node == nil:
            return None
        return node
       
    #return the minimum of a node and its subtree
    def findmin(self, node):
        while node.left != nil:
            node = node.left
        return node
        
    #return the maximum of a node and its subtree
    def findmax(self, node):
        while node.right != nil:
            node = node.right
        return node
    
    #return the successor to the given key    
    def successor(self, key):
        node = self.root
        while node.key != key:
            if node.key > key:
                if node.left != nil:
                    node = node.left
                else:
                    return node
            else:
                if node.right != nil:
                    node = node.right
                else:
                    while node.p != nil and node.p.right == node:
                        node = node.p
                    return node.p                       
        if node.right != nil:
            return self.findmin(node.right)
        while node.p != nil and node.p.right == node:
            node = node.p
        return node.p
    
    #replace node1 with node2 
    def replace(self, node1, node2 = nil):
        if node1.p == nil:
            node1 = node2
            return
        parent = node1.p
        if parent.left != nil and parent.left == node1:
            parent.left = node2
        elif parent.right != nil and parent.right == node1:
            parent.right = node2
        
    #remove a node from the tree, then balance the tree
    def remove(self, node):
        if node.left != nil and node.right != nil:
            successor = self.findmin(node.right)
            node.key = successor.key
            node.value = successor.value
            self.remove(successor)
        elif node.left != nil:
            self.replace(node, node.left)
        elif node.right != nil:
            self.replace(node, node.right)
        else: 
            self.replace(node)
        self.balance(node)
    #find the node with the given key, then remove it from the tree 
    def delete(self, key):
        node = self.find(key)
        if node != nil:
            self.size -= 1
            return self.remove(node)
        
                
    #perform an in-order traversal of the tree, printing each node
    def inOrderTraversal(self, node = None):
        if node == None:
            node = self.root
        if node != nil:
            self.inOrderTraversal(node.left)
            print(node.key, node.value)
            self.inOrderTraversal(node.right)

'''           
T = BSTree()
T.insert('text')
T.insert('text')
T.insert('key')
T.insert('keys')
T.insert('test')
T.insert('word')
T.inOrderTraversal()
print()
T.delete('test')
T.delete('text')
T.inOrderTraversal()
print()
s = T.successor('key') 
print(s.key, s.value)
print(T.size)
'''
'''
#process stopwords.txt and put the words into a set
stopwordsfile = open('stopwords.txt', 'r')
stopwords = set()
for line in stopwordsfile:
    word = line[:-1]
    stopwords.add(word)
stopwordsfile.close() 
print(stopwords)

#process the reviews and insert the words not in stopwords into the trees
reviews = open('finefoods_cleaned.txt', 'r')
lowtree = BSTree()
hightree = BSTree()
import heapq
a = []
b = []
for line in reviews:
    rating = int(line[0])
    review = line[2:]
    words = review.split()
    if rating > 3:
        for word in words:
            if word not in stopwords:
                a.append(word)
                hightree.insert(word)
    else:
        for word in words:
            if word not in stopwords:
                b.append(word)                
                lowtree.insert(word)

'''
'''
import heapq
h = []
while lowtree.root:
    heapq.heappush(h, (lowtree.root.value, lowtree.root.key))
    lowtree.delete(lowtree.root.key)
a = heapq.nlargest(20, h)

for i in a:
    print(i)
''' 
    
'''
#words to be searhed for in the trees
finds = ['asymptotic', 'binary', 'complexity', 'depth', 'mergesort', 'quicksort', 'structure', 'theta']
#search for each word in each tree. if not found, find successor.
for word in finds:
    print(word, ':')
    n = lowtree.find(word)
    if n:
        print('  found in low ratings tree')
    else:
        print(' ', lowtree.successor(word).key)
    n = hightree.find(word)
    if n:
        print('  found in high ratings tree')
    else:
        print(' ', hightree.successor(word).key)
'''
       

