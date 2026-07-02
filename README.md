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
game
│
├── main.py #loop principal
│
├── classes
│   │
│   ├── player.py #define o player
│   ├── obstacles.py #define os obstáculos
│   ├── spawner.py #define o aparecimento de obstáculos
│   ├── heart.py #define os corações
│   └── fish.py #define os peixes
|
├── utils
│   │
│   ├── colision.py #cria as colisões
│   └── texts.py #aparição dos textos
│
└── assets
    │
    ├── images #armazena as imagens
    │
    └── sounds #armazena os sons
```
---

## 🚀 Como Rodar o Jogo

O projeto possui um inicializador automático que instala o Python (se necessário) e o Pygame em um ambiente virtual isolado, funcionando no **Windows** e **Linux/macOS**.

### Método 1: Pelo VS Code (Recomendado)
1. Abra a pasta do projeto no VS Code.
2. Abra a Paleta de Comandos (`Ctrl + Shift + P`).
3. Selecione **Run Task** (ou *Executar Tarefa*) e escolha **Jogar Fish Hunter**.

### Método 2: Pelo Terminal
Abra o terminal na pasta do projeto e execute o comando correspondente ao seu sistema:

- **Windows:**
  ```powershell
  .\run.bat
  ```

- **Linux / macOS:**
  ```bash
  chmod +x run.sh && ./run.sh
  ```

---

## 👨‍💻 Equipe

Projeto desenvolvido como requisito avaliativo da disciplina de **Introdução à Programação**, ministrada pelo **Centro de Informática (CIn)** da **Universidade Federal de Pernambuco (UFPE)**, no período letivo **2026.1**.

---

## 📜 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos.
