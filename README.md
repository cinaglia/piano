Piano
=======

A little snippet that lets users pretend to be typing extremely fast.

Behind the scenes
-------

This is a python script that loads the content of a given file and outputs its characters incrementally as you
press random keys in the keyboard. It uses curses to print the text on the screen.

Usage
-------

You might want to make it an executable `chmod +x piano.py` and save it somewhere within your PATH. 

```bash
# 1. Run it against itself, inception.
./piano.py piano.py

# 2. ????
# 3. PROFIT!!!

```

(Un)License
-------
[Public domain](LICENSE)
