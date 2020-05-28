def sqrt(target=None):
    if target==None:
        return None
    answer=0
    while 1:
        if answer*answer==target:
            return answer
        answer+=1
print ("Pass" if  (None == sqrt()) else "Fail")  #test without input
print ("Pass" if  (0 == sqrt(0)) else "Fail") #test for value 0
print ("Pass" if  (4 == sqrt(16)) else "Fail") #test for a random value
print ("Pass" if  (1 == sqrt(1)) else "Fail") #test for 1
print ("Pass" if  (15 == sqrt(225)) else "Fail") #test for a large value

