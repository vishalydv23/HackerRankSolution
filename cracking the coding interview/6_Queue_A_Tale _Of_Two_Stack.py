class MyQueue(object):
    def __init__(self):
        self.old_to_new = []
        self.new_to_old = []
    
    def peek(self):
        if not self.new_to_old:
            while self.old_to_new:
                self.new_to_old.append(self.old_to_new.pop())
        val = self.new_to_old.pop()
        self.new_to_old.append(val)
        return val
        
    def pop(self):
        if not self.new_to_old:
            while self.old_to_new:
                self.new_to_old.append(self.old_to_new.pop())
        return self.new_to_old.pop()
        
        
    def put(self, value):
        self.old_to_new.append(value)
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
