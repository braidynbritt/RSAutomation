@ECHO off

ECHO "Installing Notepad++"
timeout /t 2 >NUL
start winget install --id Notepad++.Notepad++
ECHO "Installing Python3"
timeout /t 2 >NUL
start winget install --id Python.Python.3.12
ECHO "Installing Pip"
timeout/t 2 >NUL
start python get-pip.py
ECHO "Installing pyautogui"
timeout/t 2 >NUL
start pip install pyautogui
ECHO "Installing simple_colors"
timeout/t 2 >NUL
start pip install simple_colors
ECHO "Installing traceback"
timeout/t 2 >NUL
start pip install traceback
