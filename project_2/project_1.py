hi={}
class Node:
    def __init__(self,value):
        self.data=value
        self.front=None
        self.next=None
class LRUCache:
    def __init__(self,value):
        if value<=0:
            print("Cache size must be greater than Zero.")
            self.capacity=0
            return 
        self.head=None
        self.tail=None
        self.size=0
        self.capacity=value

    def put(self,key,value):
        if self.head==None:
            self.head=Node(value)
            self.tail=self.head
            hi[self.head]=key
            self.size+=1
        else:
            if self.size==self.capacity:
                del hi[self.head]
                self.head.next.front=None
                self.head=self.head.next
                self.size-=1
            new=Node(value)
            self.tail.next=new
            new.front=self.tail
            self.tail=new
            hi[new]=key
            self.size+=1
    def get(self,key):
        new=None
        for i,j in hi.items():
            if j==key:
                new=i
                break
        if not new:
            return -1
        if new==self.tail:
            return self.tail.data
        if new==self.head:
            self.head.next.front=None
            self.head=self.head.next
        else:
            new.front.next=new.next
            new.next.front=new.front    
        new.front=self.tail
        temp=self.tail
        self.tail=new
        temp.next=new
        new.next=None
        return self.tail.data
    def print_data(self):
        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
        print('\n')
our_cache=LRUCache(0)
our_cache=LRUCache(-1)
our_cache=LRUCache(5)
if our_cache.capacity:
    print(our_cache.get(1)) #return -1 as there are no values in LRU
    our_cache.put(1,1)
    our_cache.put(2,2)
    our_cache.put(3,3)
    our_cache.put(4,4)
    our_cache.print_data() #cahe data 
    print(our_cache.get(1)) #print 1
    print(our_cache.get(2)) #print 2
    print(our_cache.get(2)) #print 2
    print(our_cache.get(9)) #print -1
    our_cache.put(5,5)
    our_cache.put(6,6)
    print(our_cache.get(3)) #print -1
    print(our_cache.get(5)) #print 5
    our_cache.print_data() 
    our_cache.put(7,7)
    print(our_cache.get(4)) #print -1
    our_cache.print_data()  #cahe data 