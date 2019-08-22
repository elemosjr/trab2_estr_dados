#!/bin/python
import random
NUM_ELEMENTS = 1000

## Definindo classe Node para utilizar na classe Stack
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


## Classe Stack para ser utilizada no Deque
class Stack:
    def __init__(self):
        self.first_node = None

    def __len__(self):
        i = 0
        node = self.first_node
        while node is not None:
            i += 1
            node = node.next
        return i

    def __str__(self):
        node = self.first_node
        string = ""
        while node is not None:
            string += f"{node.value} "
            node = node.next
        return string

    def empty(self):
        if len(self) is 0:
            return True
        else:
            return False

    def push(self, value):
        new_node = Node(value)
        if self.first_node is None:
            self.first_node = new_node
        else:
            node = self.first_node
            while node.next is not None:
                node = node.next
            node.next = new_node
            new_node.prev = node

    def pop(self):
        if self.first_node is None:
            return False
        else:
            node = self.first_node
            while node.next is not None:
                node = node.next
            if node.prev is None:
                self.first_node = None
            else:
                node.prev.next = node.next
            return node.value


class Deque:
    def __init__(self):
        self.right = Stack()
        self.left = Stack()

    def __str__(self):
        node = self.left.first_node
        left = Stack()
        string = ""
        while node is not None:
            left.push(str(node.value))
            node = node.next
        while not left.empty():
            string += f"{left.pop()} "
        node = self.right.first_node
        while node is not None:
            string += f"{node.value} "
            node = node.next
        return string

    def __len__(self):
        return len(self.left)+len(self.right)

    def append(self, element):
        self.right.push(element)

    def appendleft(self, element):
        self.left.push(element)

    def pop(self):
        if self.right.empty():
            while not self.left.empty():
                self.right.push(self.left.pop())
            return self.right.pop()
        return self.right.pop()

    def popleft(self):
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