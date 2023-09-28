from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def __repr__(self):
        return f'{self.container}'

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        if not self.is_empty():
            return self.container[-1]
        else:
            return ' '
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)

#Write a function in python that can reverse a string using stack data structure.    
#reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

    def reverse_string(self, st):
        for i in st:
            self.push(i)
        k = ''
        while self.is_empty() == False:
            k += self.pop()

        return k
    
def match(m):
    p = {
        ']' : '[',
        '}' : '{',
        ')' : '('
    }
    return p[m]

def paranthesis_check(st):
    stack = Stack()
    c = 0
    for i in st:
        if i in ['(','[','{']:
            stack.push(i)
            c = 1
        if i in [')','}',']']:
            if stack.peek() != match(i):
                return False
            stack.pop()
            
    if stack.size() == 0 and c:
        return True
    return False


print(paranthesis_check('({a+b})'))
print(paranthesis_check('))((a+b}{'))
print(paranthesis_check('((a+b))'))
print(paranthesis_check('))'))
print(paranthesis_check('[a+b]*(x+2y)*{gg+kk}')) 