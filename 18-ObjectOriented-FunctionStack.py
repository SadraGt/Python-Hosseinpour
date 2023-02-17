Size = 10 
Top = -1
Sl = [-1]*Size 
def push(x):
    global Top
    if Top == 9:
        raise Exception("Stack is full")
    else:
        Top += 1
        Sl[Top] = x
    
def pop():
    global Top
    if Top == -1:
        raise Exception("Stack is empty")
    Sl[Top] = -1
    x = Sl[Top]
    Top -= 1
    return x

push(10)
push(20)
push(20)
push(30)
push(40)
push(50)
push(60)
push(70)
push(80)
push(90)
print(Sl)
pop()
print(Sl)
push(1000)
push(1111)

