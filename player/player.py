import curses
import time
import typing as t
import json

class DumbPlayer:

    def __init__(self, content: t.List[dict]):
        self.content = content
        self.content[-1]['timestamp'] += 0.3

    def decorate(self, win):
        win.addstr(0, 0, "========================TEXT-PLAY========================")
        for i in range(1, 30):
            win.addstr(i, 0, '||')
            win.addstr(i, 57, '||')
        win.addstr(30, 0, '='*58)
    
    def show_entry(self, win, entry):
        win.clear()
        self.decorate(win)
        win.addstr(1, 2, entry["buffer"])
        win.refresh()

    def play(self):
        win = curses.initscr()
        curses.cbreak()
        curses.noecho()

        start_time = time.time()
        for i, entry in enumerate(self.content):
            self.show_entry(win, entry)
            curr_time = time.time() 

            if i != len(self.content) -1:
                next_time = start_time+self.content[i+1]['timestamp']
                time.sleep(max(next_time-curr_time, 0))

        win.getch()
        curses.echo()
        curses.nocbreak()
        curses.endwin()


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            content = json.load(f)
            player = DumbPlayer(content)
            player.play()
