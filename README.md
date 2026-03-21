# 🚀 Cálculo de Volume em Tanque Esférico (Método de Newton-Raphson)

Este projeto foi desenvolvido como um desafio de aplicação prática para a disciplina de **Cálculo Numérico**. O objetivo é determinar a **altura exata ($h$)** de um líquido dentro de um tanque esférico para atingir um volume específico, utilizando o **Método de Newton-Raphson**.

---

## 📋 O Desafio de Engenharia

Imagine um tanque perfeitamente esférico com raio $R = 3$ metros. Precisamos abastecê-lo com exatamente $30$ $m^3$ de um produto químico. Como a medição é feita por uma régua vertical (sensor de nível), precisamos converter o volume desejado na altura correspondente.

### A Matemática por trás

O volume $V$ de uma calota esférica é dado pela fórmula:
$$V = \frac{\pi h^2}{3}(3R - h)$$

Para resolver o problema via Newton-Raphson, precisamos encontrar a raiz da função $f(h) = 0$. Substituindo $R = 3$ e $V = 30$:

1.  **Função Objetivo:**
    $$f(h) = \frac{\pi h^2}{3}(9 - h) - 30$$

2.  **Derivada da Função:**
    $$f'(h) = \pi h (6 - h)$$

O método atualiza o palpite inicial ($h_n$) iterativamente através da fórmula:
$$h_{n+1} = h_n - \frac{f(h_n)}{f'(h_n)}$$

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**: Linguagem principal.
* **Biblioteca Math**: Para operações precisas com $\pi$.

---

## 🚀 Como Executar o Código

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
    ```
2.  Navegue até a pasta e execute o script:
    ```bash
    python calculo_tanque.py
    ```


    ##### Desenvolvido por: Luciano Nascimento, Lucas Henrique, Lucas Vinícius & Antonio Giannini
