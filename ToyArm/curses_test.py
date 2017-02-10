#!/usr/bin/python

import curses, time

#--------------------------------------
def input_char(message):
    try:
        win = curses.initscr()
        win.addstr(0, 0, message)
        while True: 
            ch = win.getch()
            if ch in range(32, 127): break
            time.sleep(0.05)
    except: raise
    finally:
        curses.endwin()
    return chr(ch)
#--------------------------------------
c = input_char('Press s or n to continue:')
if c.upper() == 'S':
    print 'YES'

