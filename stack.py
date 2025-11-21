class stack :
    def __init__(self):
        self.elements = []
        self.last_index = -1

    def get_size(self) -> int :
        return self.last_index + 1
    
    def is_empty(self) -> bool :
        return self.get_size() ==0
    
    def push (self,value):
        self.elements.append(value)
        self.last_index += 1

    def pop (self):
        if self.is_empty():
            raise IndexError ("stack is empty - cannot pop ")
        self.last_index -=1
        return self.elements.pop()
    
    def peek(self) -> object :
        if self.is_empty():
            raise IndexError ("stack is empty - cannot peek ")
        return self.elements [self.last_index]