@echo off

:: Open ollama run phi3 in a new Command Prompt window
start "Ollama Server" cmd /k "ollama run phi3"

:: Open python3 src/main.py in a new Command Prompt window
start "Python Server" cmd /k "python3 src/main.py"

:: The /k switch keeps the Command Prompt window open after the command completes
