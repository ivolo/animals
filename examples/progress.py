
import requests
from random import randint
from time import sleep


def getTerminalSize():
    import os
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


ANIMAL_URL = 'http://localhost'


def next_frame(index=0, offset=0, reverse=False, maxwidth=0, maxheight=0):

    payload = {
        "index": index,
        "offset": offset,
        "reverse": reverse,
        "maxwidth": maxwidth,
        "maxheight": maxheight
    }

    return '\033[2J' + requests.get(ANIMAL_URL, params=payload).text


dims = getTerminalSize()

index = randint(0, 500)

counter = 0
increment = 1
offset = 0
steps = 10
reverse = False

while True:
    offset = (offset + increment)
    if offset % steps == 0:
        reverse = not reverse
        increment = -1 * increment
        dims = getTerminalSize()

    animal = next_frame(index, offset, reverse,
        maxwidth=dims[0], maxheight=dims[1])

    animal_width = len(animal.split('\n')[0]) - offset
    steps = dims[0] - animal_width

    print animal

    sleep(0.05)
