#!/bin/python
import random
NUM_ELEMENTS = 1000

class Stack():
    def __init__(self):
        self.stack = []

    def __str__(self):
        string = ""
        for i in self.stack:
            string += f"{i} "
        return string

    def __len__(self):
        return len(self.stack)

    def empty(self):
        if len(self.stack) is 0:
            return True
        else:
            return False
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.empty():
            return False
        else:
            return self.stack.pop()


class Deque:
    def __init__(self):
        self.right = Stack()
        self.left = Stack()

    def __str__(self):
        string = ""
        for i in reversed(self.left.stack):
          string += f"{i} "
        for i in self.right.stack:
          string += f"{i} "
        return string

    def __len__(self):
        return len(self.left)+len(self.right)

    def append(self, value):
        self.right.push(value)

    def appendleft(self, value):
        self.left.push(value)

    def pop(self):
        if (self.right.empty()) & (self.left.empty()):
            return False
        if self.right.empty():
            while not self.left.empty():
                self.right.push(self.left.pop())
            return self.right.pop()
        return self.right.pop()

    def popleft(self):
        if (self.right.empty()) & (self.left.empty()):
            return False
        if self.left.empty():
            while not self.right.empty():
                self.left.push(self.right.pop())
            return self.left.pop()
        return self.left.pop()

def test_simple():
    dq = Deque()  # Fila que tem "duas pontas"

    assert dq.append(10) is None  # Append 10 e nao retorna nada.
    assert dq.append(20) is None  # Append 20 e nao retorna nada.
    assert dq.append(30) is None  # ...
    assert dq.append(40) is None

    assert dq.pop() == 40  # Pop retorna 40 (pop tira da direita)
    assert dq.pop() == 30  # ...
    assert dq.pop() == 20
    assert dq.pop() == 10

    assert dq.pop() is False  # Deque vazia.
    assert dq.pop() is False  # ...

    assert dq.appendleft(40) is None
    assert dq.appendleft(50) is None

    assert dq.popleft() == 50

    assert dq.append(100) is None
    assert dq.append(200) is None

    assert dq.popleft() == 40
    assert dq.pop() == 200

    assert dq.appendleft(300) is None

    assert dq.pop() == 100
    assert dq.pop() == 300
    assert dq.pop() is False  # Deque vazia.
    assert dq.popleft() is False  # Deque vazia.


def test_random():
    dq = Deque()

    append, appendleft, = [], []
    for _ in range(NUM_ELEMENTS):
        element = random.randint(-1000, 1000)
        if random.random() > 0.5:  # Probabilidade de 50%
            dq.append(element)
            append.append(element)
        else:
            dq.appendleft(element)
            appendleft.append(element)

    for element in reversed(append):
        assert dq.pop() == element

    for element in reversed(appendleft):
        assert dq.popleft() == element

    assert dq.pop() is False  # Deque vazia.
    assert dq.popleft() is False  # Deque vazia.


def main():
    test_simple()
    test_random()


if __name__ == '__main__':
    main()