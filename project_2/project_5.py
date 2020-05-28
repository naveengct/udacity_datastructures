import hashlib
from datetime import datetime

class Link():
    def __init__(self):
        self.head=None
        self.tail=self.head
    def insert(self,data):
        if len(data)==0:
            print("Input valur can't be empty.")
            return
        new=Block(data)
        if self.head==None:
            self.head=new
            self.tail=self.head
            return
        new.previous_hash=self.tail.hash
        self.tail.next=new
        self.tail=new
    def print_val(self):
        temp=self.head
        if not temp:
            print("Empty Chain")
        while temp:
                print("-------------")
                print("DATA:",temp.data)
                print("TIMESTAMP:",temp.timestamp)
                print("HASH:",temp.hash)
                print("PRE_HASH:",temp.previous_hash)
                print("-------------")
                temp=temp.next
        print("\n")
        
class Block:
    def __init__(self, data):
      self.timestamp = datetime.now()
      self.data = data
      self.previous_hash =0
      self.hash = self.calc_hash()
      self.next=None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

a=Link()
a.print_val()#empty
a.insert("hi")
a.insert("bye")
a.insert("")
a.insert("Welcome")
a.insert("Morning")
a.print_val()
a.insert("")
