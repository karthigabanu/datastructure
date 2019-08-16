class stack:
    def __init__(self):
        self.stack=[]
    def add(self,data):
         if data not in self.stack:
            self.stack.append(data)
            return (True)
         else:
            return False
    def peek(self):
        return self.stack[-1]
    def push(self,data):
        self.stack.append(data)
        return self.stack
    def pop(self):
        if len(self.stack)<=0:
            return 'no element'
        else:
            return (self.stack.pop())
    def size(self):
        return len(self.stack)
    def print(self):
        print(self.stack)
s=stack()
s.push(4)
s.push('dog')
s.print()
print(s.peek())
s.push(True)
print(s.size())
s.push(8.4)
print(s.pop())
print(s.pop())
s.print()
print(s.size())
