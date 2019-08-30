#!/bin/python
import random
NUM_ELEMENTS = 1000

class Stack:
  def __init__(self):
    self.lista = []
  
  def __len__(self):
    return len(self.lista)

  def __str__(self):
    string = ""
    for i in self.lista:
      string += f"{i} "
    return string

  def push(self, valor):
    self.lista.append(valor)

  def pop(self):
    return self.lista.pop()

  def vazio(self):
    return len(self.lista) is 0


class Deque:
  def __init__(self):
    self.direita = Stack()
    self.esquerda = Stack()

  def __len__(self):
    return len(self.direita)+len(self.esquerda)

  def __str__(self):
    string = ""
    for i in reversed(self.esquerda.lista):
      string += f"{i} "
    for i in self.direita.lista:
      string += f"{i} "
    return string

  def append(self, valor):
    self.direita.push(valor)

  def appendleft(self, valor):
    self.esquerda.push(valor)

  def pop(self):
    if (self.direita.vazio()) & (self.esquerda.vazio()):
      return False
    elif self.direita.vazio():
      while not self.esquerda.vazio():
        self.direita.push(self.esquerda.pop())
      return self.direita.pop()
    return self.direita.pop()

  def popleft(self):
    if (self.direita.vazio()) & (self.esquerda.vazio()):
      return False
    elif self.esquerda.vazio():
      while not self.direita.vazio():
        self.esquerda.push(self.direita.pop())
      return self.esquerda.pop()
    return self.esquerda.pop()


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
