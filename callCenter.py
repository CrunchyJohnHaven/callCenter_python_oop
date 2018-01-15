#Call Center
#Summary:
# I display a list of callers and record the number of callers in a queue: int print. 
# I create and run a .remove method that removes the first caller in the list and decrements 
#the number of calls listed in the queue when I reprint the list. 

#  Operations: 
# I initialize the call object 
# with an initializing method ... def__init__ ... 
# accepts a list of call attributes - (self, name, uniqueID, number, time, and reason)
# assign the attributes to a set of variables - self.name = name, self.uniqueID, self.number, self.time, self.reason
#- I create a def display(self) method that prints the attributes, 

# I create a subclass of callCenter(object)
# I create an __init__ method that defines two attributes of the subclass - self.call, and self.queue
# I define three more methods within the callCenter Class  
# the callcenter applies 3x methods to the lists - callCenter(info): , add, remove
#def info method accepts self and newCalls as arguments, and uses the attribute self.call (empty list) with a .append method to add newCalls to the empty .calls list

# I add five instances to the list with the arguments (self,.add method
# I display the list with the five added calls with the .info method

class Call(object):
    def __init__(self, name, uniqueID, number, time, reason):
        self.name = name
        self.uniqueID = uniqueID
        self.number = number
        self.time = time
        self.reason = reason
    def display(self):
        print ' '
        print self.name
        print self.time
        print self.number
        print self.reason
class CallCenter(object):
    def __init__(self):
        self.queue = 0 
        self.calls = []

    def add(self, newCalls):
        x = len(self.calls)
        # still working on a way to reposition calls within the list based on the time that they were received
        # while x > 0:
        #     if self.time < self.lastTime:
        #         y = self.calls[x]
        #         self.calls[x] = self.newCalls
        #         self.newCalls = y
        self.calls.append(newCalls)
        self.queue += 1
        return self

    def remove(self):
        if self.queue > 0:
            del self.calls[0]
            self.queue -= 1
        return self

    def info(self):
        for i in self.calls:
            i.display()
        print "---------Queue: {}".format(self.queue)
        
cll1 = Call("Maggie", 123, 2078078436, 900, "saying hey")
cll2 = Call("Chris", 456, 8078436207, 1000, "oh hey there")
cll3 = Call("Matti", 567, 8437207807, 1100, "hey, who goes there")

cll = CallCenter()
cll.add(cll1)
cll.add(cll3)
cll.add(cll2)


cll.info()
cll.remove()
cll.info()