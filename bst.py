class Node():
        
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

class BST():   
    
    def addNode(self, root, data):
        if root == None:
            root = Node(data)
            return root
        
        temp = root

        while temp!=None:
            temp2 = temp
            if(data < temp.data):
                temp = temp.left
            else:
                temp = temp.right
        
        if data < temp2.data:
            temp2.left = Node(data)
        else:
            temp2.right = Node(data)
        
        return root
    
    def searchKey(self, root, key):
        found = False
        temp = root

        while(temp!=None):
            if(temp.data == key):
                found = True
                break
            if(key < temp.data):
                temp = temp.left
            else:
                temp = temp.right
        return found
    
    def deleteKey(self, root, key):
        temp = root
        found = False
        while(temp!=None):
            if key<temp.data:
                if(temp.left.data  == key):
                    temp = temp.left
                    print("deleted node is ", temp.data,"\n")
                    found = True
                    break
                else:
                    temp = temp.left
            else:
                if(temp.right.data  == key):
                    temp = temp.right
                    print("deleted node is ", temp.data,"\n")
                    found = True
                    break
                else:
                    temp = temp.right
            
        if(found):
            if(temp.left == None and temp.right == None):
                temp.data = None
                return
            else:
                temp2 = temp
                while(temp2!=None):
                    if temp2.left == None:
                        temp.data = temp2.data
                        temp2.data = None
                        break
                    temp2 = temp2.left
                

        
    
    def printTree(self, root):
        if(root == None):
            return
        self.printTree(root.left)
        print(root.data , " -> ", end="")
        self.printTree(root.right)

def driver():
    bst =  BST()
    values = [5,4,2,3,1,7]
    root = None
    for value in values:
        root = bst.addNode(root, value)
    found = bst.searchKey(root, 3)
    print("\nData found  == ", found,"\n")
    bst.deleteKey(root, 2)
    print("printing final inorder tree\n")
    bst.printTree(root)

driver()