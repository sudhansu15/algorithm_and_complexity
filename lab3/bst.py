class BinarySearchTree:
    def __init__(self):
        self._size = 0
        self._root = None
    
    class _BSTNode:
        def __init__(self,key,value):
            self.key =  key
            self.value = value
            self.right = None
            self.left = None                     
            self.parent = None                   

    def add(self,key,value):
        newNode = self._BSTNode(key,value)  
        compareNode = None
        rootNode = self._root
        while(rootNode!= None):
            compareNode = rootNode  #here, the compare node is updated only after rootnode i.e,  
            if(key<rootNode.key):   ## rootnode=null, then compareNode = parent
                rootNode = rootNode.left
            else:
                rootNode = rootNode.right
        if(compareNode == None): # i.e, root condition  with no parent
             self._root = newNode
        elif(newNode.key < compareNode.key):
            compareNode.left = newNode
            compareNode = newNode.parent
        else:
            compareNode.right = newNode
            compareNode = newNode.parent
        
        self._size += 1
        


    def size(self):
        return self._size
    
    def search(self,key):
        newNode =self._root
        while(newNode!=None):
            if(key == newNode.key):
                return newNode.value
            elif(key<newNode.key):
                newNode = newNode.left
            else:
                newNode = newNode.right
        return False
    
    def smallest(self):
        newNode = self._root
        while(newNode.left!=None):
            newNode = newNode.left
        return (newNode.key,newNode.value)
    
    def largest(self):
        newNode = self._root
        while(newNode.right!=None):
            newNode = newNode.right
        return (newNode.key,newNode.value)
    

                
    def delete_node(self,root, key):
        if root is None:
            return False

        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                self._size -= 1
                return root.right
            elif root.right is None:
                self._size -= 1
                return root.left
            else:
                temp = self.largestLeft(root.left)
                root.key = temp.key
                root.left = self.delete_node(root.left, temp.key)
        return root 
             
                
        
   
   
    
    def remove(self,key):
    
        root = self._root
        self.delete_node(root,key)

    
    def largestLeft(self,node):
        while node.right is not None:
            node = node.right
        return node
    

    def inorder(self,root,array):
        if(root != None):
            self.inorder(root.left,array)
            array.append(root.key)
            self.inorder(root.right,array)
        return array

    def inorder_walk(self):
        root = self._root
        array = []
        self.inorder(root,array)
        return array
    

    def preorder(self,root,array):
        if(root != None):
            array.append(root.key)
            self.preorder(root.left,array)
            self.preorder(root.right,array)
        return array

    def preorder_walk(self):
        root = self._root
        array = []
        self.preorder(root,array)
        return array
        
    
    def postorder(self,root,array):
        if(root != None):
            self.postorder(root.left,array)
            self.postorder(root.right,array)
            array.append(root.key)
        return array

    def postorder_walk(self):
        root = self._root
        array = []
        self.postorder(root,array)
        return array
            

    

        


        



