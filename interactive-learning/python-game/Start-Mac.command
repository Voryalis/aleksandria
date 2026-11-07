#!/bin/zsh
cd -- "$(dirname -- "$0")"
python3 game.py
printf '\nPress Enter to close this window.\n'
read reply