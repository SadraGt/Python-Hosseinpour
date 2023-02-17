class Stack:
    def __init__(self, n) -> None:
        self.Size = n
        self.Top = -1
        self.Sl = [-1]*self.Size 
    
        
    def push(self, x):
        if self.Top == self.Size - 1:
            raise Exception("Stack is full")
        else:
            self.Top += 1
            self.Sl[self.Top] = x
    
    def pop(self):
        if self.Top == -1:
            raise Exception("Stack is empty")
        self.Sl[self.Top] = -1
        x = self.Sl[self.Top]
        self.Top -= 1
        return x
    def pr(self):
        print(self.Sl)
        