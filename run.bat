@echo off
setlocal enabledelayedexpansion

echo ===================================================
echo         Fish Hunter - Inicializador Automático
echo ===================================================
echo.

:: 1. Verificar se o Python está no PATH
python --version >nul 2>&1
if %errorlevel% equ 0 (
    set "PYTHON_CMD=python"
    echo [+] Python detectado no PATH do sistema.
    goto check_venv
)

:: 2. Verificar se o Python está instalado no caminho padrão do usuário (Appdata)
set "USER_PYTHON=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
if exist "%USER_PYTHON%" (
    set "PYTHON_CMD=%USER_PYTHON%"
    echo [+] Python detectado em %USER_PYTHON%
    goto check_venv
)

:: 3. Se não encontrar, tenta instalar o Python via winget (User Scope)
echo [-] Python nao detectado no seu sistema.
echo [*] Tentando instalar o Python automaticamente via winget (sem precisar de privilegios de admin)...
echo.

winget install Python.Python.3.12 --scope user --accept-package-agreements --accept-source-agreements
if %errorlevel% neq 0 (
    echo.
    echo [ERR] Erro ao tentar instalar o Python via winget.
    echo Por favor, instale o Python manualmente em: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

:: Re-verificar se o Python agora existe após a instalação do winget
if exist "%USER_PYTHON%" (
    set "PYTHON_CMD=%USER_PYTHON%"
) else (
    :: Tenta atualizar o PATH temporariamente para encontrar o Python recém instalado
    set "PATH=%LOCALAPPDATA%\Programs\Python\Python312;%PATH%"
    python --version >nul 2>&1
    if %errorlevel% equ 0 (
        set "PYTHON_CMD=python"
    ) else (
        echo.
        echo [ERR] Python foi instalado, mas nao pudemos localizar o executavel.
        echo Por favor, reinicie o VS Code e tente rodar este script novamente.
        echo.
        pause
        exit /b 1
    )
)

:check_venv
echo.
:: 4. Criar e gerenciar ambiente virtual (.venv) no projeto
echo [*] Verificando ambiente virtual...
if not exist ".venv" (
    echo [*] Criando ambiente virtual local ^(.venv^)...
    "%PYTHON_CMD%" -m venv .venv
    if !errorlevel! neq 0 (
        echo [ERR] Erro ao criar o ambiente virtual.
        pause
        exit /b 1
    )
)

:: 5. Instalar/atualizar pygame dentro do ambiente virtual (.venv)
echo [*] Verificando dependencias ^(pygame^)...
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install pygame
if %errorlevel% neq 0 (
    echo [ERR] Erro ao instalar ou atualizar a biblioteca pygame.
    pause
    exit /b 1
)

:: 6. Executar o jogo
echo.
echo [+] Tudo pronto! Iniciando o Fish Hunter...
start "" .venv\Scripts\pythonw main.py
echo [+] O jogo foi iniciado com sucesso em segundo plano.
echo.
exit /b 0
