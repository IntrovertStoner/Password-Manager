@echo off
cd /d "%~dp0"
start /min pyw install_requirements.py
start /min pyw GUI.py