@echo off

rem Executa todas as tarefas
if "%1" == "" (
call :build
call :release
goto :EOF
)

rem Executa o build
if "%1" == "build" (
call :build
goto :EOF
)

:build
echo executando o build
echo rodando black
black mtspread
black tests
echo rodando testes
pytest -q
echo rodando build
poetry build
echo instalando local
poetry install
goto :EOF

:release
echo executando release
goto :EOF

