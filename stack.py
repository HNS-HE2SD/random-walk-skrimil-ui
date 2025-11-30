class stack :
    def __init__(self):
        self._items = []

    def is_empty(self) :
        return len(self._items) == 0

    def get_size(self) :
        return len(self._itmes)
    
    
    def push (self,value):
        self._items.append(value)

    def pop (self):
        if self.is_empty():
            raise IndexError ("stack is empty - cannot pop ")
        return self._items.pop()
    
    def peek(self) :
        if self.is_empty():
            raise IndexError ("stack is empty - cannot peek ")
        return self._items [-1]