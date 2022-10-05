class Node:
    def __init__(self,key,val):
        self.pre = None
        self.post = None
        self.val = val
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.tail = Node(0,0)
        self.head = Node(0,0)
        self.head.pre,self.tail.post = self.tail,self.head
        self.l = 0
        self.d={}
    def to_top(self,node):
        Pre,Post = node.pre,node.post
        Pre.post,Post.pre = Post,Pre

        last = self.head.pre
        last.post,self.head.pre = node,node 
        node.pre,node.post = last,self.head


    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.to_top(node)
            
            return self.d[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.to_top(node)
        
        else:
            node = Node(key,value)
            Pre = self.head.pre
            Pre.post,node.pre =node,Pre
            node.post,self.head.pre = self.head,node
            self.d[key] = node
            self.l+=1
            if self.l>self.cap:
                self.l=self.cap
                last = self.tail.post
                # print(last.key,'db')
                del self.d[last.key]
                
                self.tail = self.tail.post
                
    def print(self):
        cur = self.tail
        print("==",end=" ")
        while cur!=None:
            print(f"({cur.key} {cur.val})", end=" ")
            cur = cur.post
        print()

x = LRUCache(2)
print(x.put(2, 1) )
x.print()
print(x.put(1, 1) )
x.print()
print(x.put(2, 3) )
x.print()
print(x.put(4, 1) )
x.print()
print(x.get(1))
x.print()
print(x.get(2)    )
x.print()
# print(x.put(3, 3))
# x.print()
# print(x.get(2)    )
# x.print()
# print(x.put(4, 4) )
# x.print()
# print(x.get(1)    )
# print(x.get(3)   )
# print(x.get(4)   ) 
# x.print()