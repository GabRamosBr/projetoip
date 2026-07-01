#!/bin/bash

echo "==================================================="
echo "        Fish Hunter - Inicializador Automático"
echo "==================================================="
echo ""

# 1. Verificar se o Python 3 está instalado
if ! command -v python3 &> /dev/null; then
    echo "[-] Python3 nao esta instalado."
    echo "[*] Por favor, instale o Python 3 utilizando o gerenciador de pacotes do Ubuntu:"
    echo "    sudo apt update && sudo apt install python3 python3-pip python3-venv"
    exit 1
fi

# 2. Verificar se o ambiente virtual (.venv) já existe
if [ ! -d ".venv" ]; then
    echo "[*] Criando ambiente virtual (.venv)..."
    python3 -m venv .venv 2>/dev/null
    
    # Se falhar porque python3-venv não está instalado
    if [ $? -ne 0 ]; then
        echo "[ERR] Erro ao criar o ambiente virtual."
        echo "      Isso costuma ocorrer se o pacote 'python3-venv' nao estiver instalado."
        echo "      Instale-o executando:"
        echo "      sudo apt update && sudo apt install python3-venv"
        exit 1
    fi
fi

# 3. Instalar/atualizar dependências
echo "[*] Instalando dependencias (pygame)..."
.venv/bin/pip install --upgrade pip
.venv/bin/pip install pygame

# 4. Rodar o jogo
echo ""
echo "[+] Tudo pronto! Iniciando o Fish Hunter..."
.venv/bin/python main.py &
echo "[+] O jogo foi iniciado com sucesso em segundo plano."
echo ""
