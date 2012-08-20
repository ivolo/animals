
import os
import sys
import requests
from random import randint
from time import sleep

BASE_URL = "http://animals.ivolo.me"


# from http://stackoverflow.com/questions/566746/how-to-get-console-window-width-in-python
def getTerminalSize():
    env = os.environ

    def ioctl_GWINSZ(fd):
        try:
            import fcntl
            import termios
            import struct

            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return None
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (env['LINES'], env['COLUMNS'])
        except:
            cr = (25, 80)
    return int(cr[1]), int(cr[0])


def next_frame(index=0, offset=0, reverse=False,
    maxwidth=0, maxheight=0, terminal=False):

    payload = {
        "index": index,
        "offset": offset,
        "reverse": reverse,
        "maxwidth": maxwidth,
        "maxheight": maxheight,
        "terminal": terminal
    }

    return requests.get(BASE_URL, params=payload).text


class ProgressBar:

    def __init__(self):
        self.dims = getTerminalSize()
        # pick a random animal
        self.index = randint(0, 500)

        # how many times we've iterated
        self.counter = 0
        # specifies the direction in which the animal is offset
        self.increment = 1
        # the total offset from the left
        self.offset = 0
        # the amount of steps the animal travels before turning around
        self.steps = 10
        # whether its reverse or not
        self.reverse = False

    def step(self):
         # the amount to offset the animal from the left
        self.offset = (self.offset + self.increment)

        # if we're at the beggining or end of the screen, reverse!
        if self.offset % self.steps == 0:
            # flip direction
            self.reverse = not self.reverse
            self.increment = -1 * self.increment

            # update terminal dimensions in case they changed
            self.dims = getTerminalSize()

        # get the next frame
        animal = next_frame(self.index, self.offset, self.reverse,
            maxwidth=self.dims[0], maxheight=self.dims[1],
            terminal=(self.counter > 0))

        # split the animal into lines
        lines = animal.split('\n')
        # get how wide the animal is
        animal_width = len(lines[-1]) - self.offset
        # recalculate how many steps we can make before turning around
        self.steps = self.dims[0] - animal_width

        # write and flush the animal to standard OUT
        sys.stdout.write(animal)

        self.counter += 1


if __name__ == "__main__":

    p = ProgressBar()
    while True:
        p.step()
        sleep(0.1)
