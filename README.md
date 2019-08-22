## Implementar Deque

* Filas (Queues) são estrutura de dados que respeitam a regra do primeiro elemento
  a entrar é o primeiro a sair (FIFO);
* Fila de Duas Pontas (Double ended queue), como o nome diz, a fila tem duas
  pontas: uma à direita e outra à esquerda;
* Para inserir e remover na ponta **direita** respectivamente: `dq.append(x); dq.pop();`
  igual a fila comum.
* Para inserir e remover na ponta **esquerda** respectivamente:
  `dq.appendleft(x); dq.popleft();`
* **O objetivo principal do trabalho é implementar uma Fila de Duas Pontas**
  (`class Deque`) com algumas restrições:

    * **Apenas pilhas** devem ser as estruturas de dados interna da `Deque` para
      manipular os itens inseridos (`append`) e removidos (`pop`), logo é
      necessário implementar a estrutura de dado "Pilha" (`Stack`). Use as pilhas
      implementadas em sala de aula se achar necessário.

* Caso a *Deque* esteja vazia, **`False` deve ser retornado**;

* **Nenhum módulo** (`import`) pode ser usado para o o trabalho, incluindo o módulo
  `collections` que serve de exemplo para mostrar como a Deque deve funcionar.
