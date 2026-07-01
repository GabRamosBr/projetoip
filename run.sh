#!/bin/bash

echo "==================================================="
echo "        Fish Hunter - Inicializador Automático"
echo "==================================================="
echo ""

# 1. Escolher a melhor versão de Python disponível (preferindo as que possuem wheels prontas para Pygame)
PYTHON_BIN=""
for cmd in python3.12 python3.11 python3.13 python3; do
    if command -v "$cmd" &> /dev/null; then
        PYTHON_BIN="$cmd"
        break
    fi
done

if [ -z "$PYTHON_BIN" ]; then
    echo "[-] Python 3 nao esta instalado."
    echo "[*] Por favor, instale o Python 3 utilizando o gerenciador de pacotes do seu sistema."
    exit 1
fi

echo "[+] Python detectado: $PYTHON_BIN"

# 2. Verificar se o ambiente virtual (.venv) já existe e se foi criado com a versão correta
RECREATE_VENV=false
if [ -d ".venv" ]; then
    if [ ! -f ".venv/bin/python" ]; then
        RECREATE_VENV=true
    else
        VENV_VERSION=$(.venv/bin/python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null)
        SYS_VERSION=$("$PYTHON_BIN" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null)
        if [ "$VENV_VERSION" != "$SYS_VERSION" ]; then
            echo "[*] A versao do Python no .venv ($VENV_VERSION) difere da versao recomendada ($SYS_VERSION)."
            RECREATE_VENV=true
        fi
    fi
else
    RECREATE_VENV=true
fi

if [ "$RECREATE_VENV" = true ]; then
    echo "[*] Criando/reconfigurando ambiente virtual (.venv) com $PYTHON_BIN..."
    rm -rf .venv
    "$PYTHON_BIN" -m venv .venv 2>/dev/null
    
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

# 4. Rodar o jogo no primeiro plano para evitar que o VS Code encerre a tarefa
echo ""
echo "[+] Tudo pronto! Iniciando o Fish Hunter..."
.venv/bin/python main.py
echo "[+] Jogo finalizado."
echo ""
