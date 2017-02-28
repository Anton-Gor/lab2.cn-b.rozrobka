import numpy as np
import numpy.random as rand
rand

#random choise
t = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
t1 = 'Hearts', 'Diamonds', 'Clubs', 'Spades'

class isblock(object):
    def __init__(self, item_factory = None):
        self.item_factory=item_factory
    def get(self):
        item=self.item_factory.get_()
        print ("Key: ", item.key())
        print("Cost: ", self.item_factory.cost())
        print( "Suit: ", self.item_factory.suit())
        print ("Name: ", self.item_factory.name())

class block(object):
    def key(self):
        return "blocked"
    def __str__(self):
        return "blocked"

class unblock(object):
    def name(self):
        return "unblocked"
    def __str__(self):
        return "unblocked"

class none(object):
    def name(self):
        return "there is no any card"
    def __str__(self):
        return "there is no any card"


class blocked(object):
    def get_(self):
        return block()
    def cost(self):
        global x1
        x=np.rand.choice(t, size=1, replace=True)
        x=x1
        return x
    def suit(self):
        y=np.random.choice(t1, size=1, replace=True)
        return y
    def name(self):
        if x1==1:
            return "Ace"
        elif x1==2:
            return "Two"
        elif x1==3:
            return "Three"
        elif x1==4:
            return "Four"
        elif x1==5:
            return "Five"
        elif x1==6:
            return "Six"
        elif x1==7:
            return "Seven"
        elif x1==8:
            return "Eight"
        elif x1==9:
            return "Nine"
        elif x1==10:
            return "Ten"
        elif x1==11:
            return "Jack"
        elif x1==12:
            return "Queen"
        else:
            return "King"

a=isblock(blocked())
a.get()


class node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return 'Node ['+str(self.data)+']'

#/* класс, описывающий само дерево */
class Tree:
    def __init__(self):
        self.root = None #корень дерева

# /* функция для добавления узла в дерево */
    def newNode(self, data):
        return node(data,None,None)

# /* функция для распечатки дерева */
    def printLevelOrder(self, root):
      h = self.height(self.root)
      i=1
      while(i<=h):
        self.printGivenLevel(self.root, i)
        i +=1




#    /* функция для проверки наличия узла */
    def lookup(self, node, target):
        if node == None:return 0
        else:
            if target == node.data: return 1
            else:
                if target < node.data: return self.lookup(node.left, target)
                else: return self.lookup(node.right, target)


#класс Node для определения элемента списка
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next



class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [\n' +str(current.value) +'\n'
            while current.next != None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

#delete the head
def Del(self,i):
        if (self.first == None):
          return
        curr = self.first
        count = 0
        if i == 0:
          self.first = self.first.next
          return
        while curr != None:
            if count == i:
              if curr.next == None:
                self.last = curr
              old.next = curr.next
              break
            old = curr
            curr = curr.next
            count += 1