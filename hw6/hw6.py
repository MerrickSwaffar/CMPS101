#Python implementation of a binary search tree
class BSTree(object):
    
    #Node subclass 
    class Node(object):
        
        #Node constructor
        def __init__(self, key, value = 1, parent = None):
            self.parent = parent
            self.left = None
            self.right = None
            self.key = key
            self.value = value 
        
        #inorder traversal for a node and it's children
        def inorder(node):
            if node:
                BSTree.Node.inorder(node.left)
                print(node.key, node.value)
                BSTree.Node.inorder(node.right)
        
        #return the minimum of a node and its subtree
        def findmin(node):
            while node.left:
                node = node.left
            return node
        
        #return the maximum of a node and its subtree
        def findmax(node):
            while node.right:
                node = node.right
            return node
        
        #replace node1 with node2 
        def replace(node1, node2 = None):
            if node1.parent == None:
                node1 = node2
                return
            parent = node1.parent
            if parent.left and parent.left == node1:
                parent.left = node2
            elif parent.right and parent.right == node1:
                parent.right = node2
        
        #remove a node while maintaining the bst property
        def remove(node):
            if node.left and node.right:
                successor = node.right.findmin()
                node.key = successor.key
                node.value = successor.value
                BSTree.Node.remove(successor)
            elif node.left:
                BSTree.Node.replace(node, node.left)
            elif node.right:
                BSTree.Node.replace(node, node.right)
            else: 
                BSTree.Node.replace(node)
    
    #BSTree constructor
    def __init__(self):
        self.size = 0
        self.root = None
    
    #search for the given key in the tree. return that node if found. 
    def find(self, key):
        node = self.root
        while node:
            if key == node.key:
                return node
            if node.key > key:
                node = node.left
            else:
                node = node.right
        return None
    
    #return the successor to the node with the given key    
    def successor(self, key):
        node = self.root
        while node.key != key:
            if node.key > key:
                if node.left:
                    node = node.left
                else:
                    return node
            else:
                if node.right:
                    node = node.right
                else:
                    while node.parent and node.parent.right == node:
                        node = node.parent
                    return node.parent                       
        if node.right:
            return BSTree.Node.findmin(node.right)
        while node.parent and node.parent.right == node:
            node = node.parent
        return node.parent
        
    #insert a node with the given key and value into the tree   
    def insert(self, key, value = 1):
        node = self.root
        if node == None:
            self.size += 1
            self.root = BSTree.Node(key, value)
            return self.root
        while node:
            if node.key == key:
                node.value += value
                return node
            elif node.key > key:
                if node.left:
                    node = node.left
                else:
                    self.size += 1
                    node.left = BSTree.Node(key, value, node)
                    return node.left
            else:
                if node.right:
                    node = node.right
                else:
                    self.size += 1
                    node.right = BSTree.Node(key, value, node)
                    return node.right
    
    #delete the node with the given key, using the remove function in Node  
    def delete(self, key):
        node = self.find(key)
        if node:
            self.size -= 1
            return BSTree.Node.remove(node)
        
    #inorder traversal of a tree. calls the inorder method of Node. 
    def inOrderTraversal(self):
        return BSTree.Node.inorder(self.root) 

#below is code used for testing and questions 2-4 
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
s = T.successor('texz') 
print(s.key, s.value)
print(T.size)
T.inOrderTraversal()

#process stopwords.txt and put the words into a set
stopwordsfile = open('stopwords.txt', 'r')
stopwords = set()
for line in stopwordsfile:
    word = line[:-1]
    stopwords.add(word)
stopwordsfile.close() 
#print(stopwords)

#process the reviews and insert the words not in stopwords into the trees
reviews = open('finefoods_cleaned.txt', 'r')
lowtree = BSTree()
hightree = BSTree()

for line in reviews:
    rating = int(line[0])
    review = line[2:]
    words = review.split()
    if rating > 3:
        for word in words:
            if word not in stopwords:
                hightree.insert(word)
    else:
        for word in words:
            if word not in stopwords:              
                lowtree.insert(word)
              
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

#traverse a tree and put elements into a heap              
import heapq
def traversal(node, heap):
            if node:
                traversal(node.left, heap)
                heapq.heappush(heap, (node.value, node.key))
                print(node.value, node.key)
                traversal(node.right, heap)
    

#find top 20 in high ratings tree
h1 = []
traversal(hightree.root, h1)
a = heapq.nlargest(20,h1)
for i in a:
    print(i)
#find top 
h2 = []
traversal(lowtree.root, h2)
b = heapq.nlargest(20,h2)
for i in b:
    print(i)

#put only words not in low reviews in high review tree
reviews = open('finefoods_cleaned.txt', 'r')
lowtree = BSTree()
hightree = BSTree()
for line in reviews:
    rating = int(line[0])
    review = line[2:]
    words = review.split()
    if rating < 3:
        for word in words:
            if word not in stopwords:
                lowtree.insert(word)
reviews = open('finefoods_cleaned.txt', 'r')
for line in reviews:
    rating = int(line[0])
    review = line[2:]
    words = review.split()
    for word in words:
        if word not in stopwords and not lowtree.find(word):              
            hightree.insert(word)        
h1 = []
traversal(hightree.root, h1)
a = heapq.nlargest(20,h1)
for i in a:
    print(i)
'''