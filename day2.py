class Stack:
    def __init__(self):
        self.items=list() #스택만들면 제일 먼저하는 것: 리스트 만들기

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop() #리턴 후, 삭제

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1] #확인용도


s1=Stack()
s1.push(-9)
s1.push(11)
s1.push(977)
print(s1.pop())
print(s1.peek())
print(s1.peek())