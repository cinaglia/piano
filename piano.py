#!/usr/bin/env python

import curses
import sys
import os


class Piano:
    """
    Simulate super fast typing.

    This class reads the content of an existing file and loads it into memory.
    Regardless of what you type, it outputs the content onto the screen.
    """

    def __init__(self):
        """ Init curses """
        self.stdscr = curses.initscr()
        curses.noecho()

    def open_file(self, file_name):
        """ Read file contents into a list of characters. """
        # Read file
        with open(file_name, 'r+') as f:
            lines = f.readlines()

        # Set content as a list of characters
        self.text = list(''.join(lines))
        self.text.append('\n')
        self.text.reverse()

    def loop(self):
        """ Loop indefinitely until file is empty. """
        while True:
            self.stdscr.getch()
            if len(self.text):
                # Output last two elements from the list
                self.stdscr.addstr(self.text.pop() + self.text.pop())
                self.stdscr.refresh()
            else:
                pass

    def close(self):
        """ Close out curses to avoid the nasty bug when quitting it. """
        curses.nocbreak()
        curses.echo()
        curses.endwin()

if __name__ == "__main__":
    # Ensure expected arg is defined
    if len(sys.argv[1:]) != 1:
        print "Expected parameter not provided [file_name]."
        sys.exit()

    try:
        piano = Piano()
        piano.open_file(sys.argv[1])
        piano.loop()
    except (Exception, KeyboardInterrupt) as e:
        piano.close()

        # Handle file not found exception
        if isinstance(e, IOError):
            print "File not found"
