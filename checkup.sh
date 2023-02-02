#!/bin/bash
(ls core/main.py >> /dev/null 2>&1 && echo "core/main.py [OK]") || echo "core/main.py [ERROR]"
(ls core/motors/turn.py >> /dev/null 2>&1 && echo "core/motors/turn.py [OK]") || echo "core/motors/turn.py [ERROR]"
(ls core/motors/game.py >> /dev/null 2>&1 && echo "core/motors/game.py [OK]") || echo "core/motors/game.py [ERROR]"
echo press enter
read -n 1 -s