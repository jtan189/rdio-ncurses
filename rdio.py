#!/usr/bin/env python

import argparse
import curses
import sys
import urllib
import urlparse

import rdioapi

def main(args):
    screen = curses.initscr() 
    curses.noecho() 
    curses.curs_set(0) 
    screen.keypad(1) 

    # show playlists
    for i in range(20):
        screen.addstr("Playlist %d\n" % (i+1))
    screen.addstr("\nPress 'q' to quit.")

    while True:
       event = screen.getch() 
       if event == ord("q"):
           break 

    curses.endwin()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ncurses interface to rdio')
    parser.add_argument('--key', help='Rdio API key')
    parser.add_argument('--secret', help='Rdio API secret')
    parser.add_argument('--token', help='Rdio API access token')
    args = parser.parse_args()
    main(args)
