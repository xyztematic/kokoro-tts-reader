@echo off
python -m venv .
call .\Scripts\activate.bat
pip install kokoro soundfile kivy
