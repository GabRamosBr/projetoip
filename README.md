# projetoip - 🎣 Fish Hunter

Repositório referente ao desenvolvimento do Projeto Final da Unidade da disciplina de **Introdução à Programação** do **Centro de Informática da Universidade Federal de Pernambuco (CIn/UFPE)** – período **2026.1**.

---

## 📖 Sobre o Projeto

**Fish Hunter** é um jogo de pescaria desenvolvido em **Python**, utilizando os conceitos de **Programação Orientada a Objetos (POO)**.

O objetivo do jogador é capturar apenas os peixes saudáveis que aparecem no cenário, acumulando pontos e sobrevivendo o maior tempo possível. Para isso, será necessário desviar de diversos obstáculos espalhados pelo ambiente, como lixo, espinhas de peixe e pedras, que podem reduzir suas vidas.

Além disso, corações poderão surgir durante a partida para ajudar o jogador a recuperar vidas perdidas.

---

## 🎯 Objetivo

- Capturar os peixes bons para aumentar a pontuação.
- Coletar corações para recuperar vidas.
- Evitar obstáculos que causam dano.
- Sobreviver o máximo de tempo possível.
- Alcançar a maior pontuação ao final da partida.

---

## 🎮 Mecânicas do Jogo

### Itens Coletáveis

🐟 **Peixes Bons**
- Concedem pontos ao jogador.

❤️ **Corações**
- Recuperam uma vida.

### Obstáculos

🗑️ **Lixo**
- Remove uma vida ao ser atingido.

🦴 **Espinha de Peixe**
- Remove uma vida ao ser atingido.

🪨 **Pedras**
- Remove uma vida ao ser atingido.

---

## ❤️ Sistema de Vidas

O jogador inicia a partida com uma quantidade limitada de vidas.

Ao colidir com obstáculos, uma vida é perdida. Caso todas as vidas sejam consumidas, a partida é encerrada.

Corações podem ser coletados para restaurar vidas durante o jogo.

---

## 🏆 Sistema de Pontuação

| Evento | Recompensa |
|----------|----------|
| Capturar peixe bom | Pontos |
| Coletar coração | Recuperação de vida |
| Colidir com obstáculo | Perda de vida |

---

## 🛠️ Tecnologias e Conceitos

### Linguagem
- Python

### Conceitos Aplicados
- Programação Orientada a Objetos (POO)
- Classes e Objetos
- Encapsulamento
- Herança
- Polimorfismo
- Estruturas de repetição
- Estruturas condicionais
- Manipulação de eventos
- Controle de colisões

---

## 📂 Estrutura do Projeto

```text
FishHunter/
│
├── src/
│   ├── main.py
│   ├── jogador.py
│   ├── peixe.py
│   ├── obstaculo.py
│   ├── coracao.py
│   └── jogo.py
│
├── assets/
│   ├── imagens/
│   └── sons/
│
└── README.md
```

---

## 👨‍💻 Equipe

Projeto desenvolvido como requisito avaliativo da disciplina de **Introdução à Programação**, ministrada pelo **Centro de Informática (CIn)** da **Universidade Federal de Pernambuco (UFPE)**, no período letivo **2026.1**.

---

## 📜 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos.
