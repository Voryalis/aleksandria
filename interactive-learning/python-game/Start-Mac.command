#!/bin/zsh
cd -- "$(dirname -- "$0")" || exit 1

if ! python3 -c 'import sys; sys.exit(sys.version_info < (3, 9))' >/dev/null 2>&1; then
    print 'Python 3.9 or newer is required.'
    print 'Install it from https://www.python.org/downloads/ and run this launcher again.'
    read 'reply?Press Enter to close this window. '
    exit 1
fi

python3 game.py "$@"
game_exit=$?
printf '\nPress Enter to close this window.\n'
read reply
exit "$game_exit"
