"""
    Swimming fishes progress indicator
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Well, what can you say really? It's a swimming fish that animates when you
    call a certain function. Simple as that.

    How to use:

    .. code-block:: python

       import fish

       for datum_to_churn in data:
           fish.animate()
           churn_churn(datum_to_churn)

    Using other fish or birds:

    .. code-block:: python

       from fish import Bird

       bird = Bird()
       while True:
           bird.animate()
"""

import sys
import time
import string

from struct import unpack
from fcntl import ioctl
from termios import TIOCGWINSZ

from itertools import cycle, count

def get_term_width():
    """Get terminal width or None."""
    for fp in sys.stdin, sys.stdout, sys.stderr:
        try:
            return unpack("hh", ioctl(fp.fileno(), TIOCGWINSZ, "    "))[1]
        except IOError:
            continue

class ANSIControl(object):
    def __init__(self, outfile=sys.stderr, flush=True):
        self.outfile = outfile
        self.flush = flush

    def ansi(self, command):
        self.outfile.write("\x1b[%s" % command)
        if self.flush:
            self.outfile.flush()

    def clear_line_right(self): self.ansi("0K\r")
    def clear_line_left(self): self.ansi("1K\r")
    def clear_line_whole(self): self.ansi("2K\r")
    def clear_forward(self): self.ansi("0J")
    def clear_backward(self): self.ansi("1J")
    def clear_whole(self): self.ansi("2J")
    def save_cursor(self): self.ansi("s")
    def restore_cursor(self): self.ansi("u")
    def move_up(self, n): self.ansi("%dF" % n)
    def move_down(self, n): self.ansi("%dE" % n)

class SwimFishBase(object):
    def __init__(self, velocity=10, world_length=None, outfile=sys.stderr):
        if not world_length:
            world_length = get_term_width() or 79
        self.worldstep = self.make_worldstepper()
        self.velocity = velocity
        self.world_length = world_length
        self.outfile = outfile
        self.ansi = ANSIControl(outfile=outfile)
        self.last_hash = 0

    def test(self):
        while True:
            self.animate()
            time.sleep(0.1)

    @property
    def actual_length(self):
        # Refit the world so that we can move along an axis and not worry about
        # overflowing
        return self.world_length - self.own_length

    def animate(self, outfile=None, force=False):
        step = self.worldstep.next()
        # As there are two directions we pretend the world is twice as large as
        # it really is, then handle the overflow
        pos = (self.velocity * step) % (self.actual_length * 2)
        reverse = pos < self.actual_length
        pos = int(round(abs(pos - self.actual_length), 0))
        fish = self.render(step=step, reverse=reverse)
        of = outfile or self.outfile
        curr_hash = force or hash((of, pos, "".join(fish)))
        if force or curr_hash != self.last_hash:
            self.print_fish(of, pos, fish)
            of.flush()
            self.last_hash = curr_hash

    def print_fish(self, of, pos, fish):
        raise NotImplementedError("you must choose a printer type")

class SingleLineFishPrinter(SwimFishBase):
    def print_fish(self, of, pos, fish):
        lead = " " * pos
        trail = " " * (self.world_length - self.own_length - pos)
        self.ansi.clear_line_whole()
        assert len(fish) == 1
        of.write(lead + fish[0] + trail + "\r")

class MultiLineFishPrinter(SwimFishBase):
    _printed = False

    def __init__(self, *args, **kwds):
        super(MultiLineFishPrinter, self).__init__(*args, **kwds)
        self.reset()

    def reset(self):
        """Call this when reusing the animation in a new place"""
        self._printed = False

    def _restore_cursor(self, lines):
        if self._printed:
            self.ansi.move_up(lines)
        self._printed = True

    def print_fish(self, of, pos, fish):
        lead = " " * pos
        trail = " " * (self.world_length - self.own_length - pos)
        self._restore_cursor(len(fish))
        self.ansi.clear_forward()
        for line in fish:
            of.write(lead + line + trail + "\n")

class ProgressableFishBase(SwimFishBase):
    """Progressing fish, only compatible with single-line fish"""

    def __init__(self, *args, **kwds):
        total = kwds.pop("total", None)
        super(ProgressableFishBase, self).__init__(*args, **kwds)
        if total:
            # `pad` is the length required for the progress indicator,
            # It, at its longest, is `100% 123/123`
            pad = len(str(total)) * 2
            pad += 6
            self.world_length -= pad
        self.total = total

    def test(self):
        if not self.total:
            return super(ProgressableFishBase, self).test()
        for i in xrange(1, self.total * 2 + 1):
            self.animate(amount=i)
            time.sleep(0.025)

    def animate(self, *args, **kwds):
        prev_amount = getattr(self, "amount", None)
        self.amount = kwds.pop("amount", None)
        if self.amount != prev_amount:
            kwds["force"] = True
        return super(ProgressableFishBase, self).animate(*args, **kwds)

    def print_fish(self, of, pos, fish):
        if not self.amount:
            return super(ProgressableFishBase, self).print_fish(of, pos, fish)

        # Get the progress text
        if self.total:
            part = self.amount / float(self.total)
            done_text = str(self.amount).rjust(len(str(self.total)))
            progress = "%3.d%% %s/%d" % (part * 100, done_text, self.total)
        else:
            progress = str(amount)

        lead = " " * pos
        trail = " " * (self.world_length - self.own_length - pos)
        self.ansi.clear_line_whole()
        assert len(fish) == 1
        of.write(lead + fish[0] + trail + progress + "\r")

class BassLook(SingleLineFishPrinter):
    def render(self, step, reverse=False):
        return ["<'((<" if reverse else ">))'>"]

    own_length = len(">))'>")

class SalmonLook(SingleLineFishPrinter):
    def render(self, step, reverse=False):
        return ["<*}}}><" if reverse else "><{{{*>"]

def docstring2lines(ds):
    return filter(None, ds.split("\n"))
rev_trans = string.maketrans(r"/\<>76", r"\/></9")
def ascii_rev(ascii):
    return [line.translate(rev_trans)[::-1] for line in ascii]

class BirdLook(MultiLineFishPrinter):
    # ASCII credit: "jgs"
    bird = r"""
           ___     
       _,-' ______ 
     .'  .-'  ____7
    /   /   ___7   
  _|   /  ___7     
>(')\ | ___7       
  \\/     \_______ 
  '        _======>
  `'----\\`        
"""
    bird = docstring2lines(bird)
    bird_rev = ascii_rev(bird)

    def render(self, step, reverse=False):
        return self.bird if reverse else self.bird_rev

    own_length = len(bird[0])

class DuckLook(MultiLineFishPrinter):
    # ASCII art crediT: jgs
    duck = docstring2lines("""
     _ 
\. _(9>
 \==_) 
  -'=  
""")

    duck_rev = docstring2lines("""
 _     
<6)_ ,/
 (_==/ 
  ='-  
""")

    def render(self, step, reverse=False):
        return self.duck_rev if reverse else self.duck

    own_length = len(duck[0])


class SwimFishNoSync(SwimFishBase):
    @classmethod
    def make_worldstepper(cls):
        return count()

class SwimFishTimeSync(SwimFishBase):
    @classmethod
    def make_worldstepper(cls):
        return iter(time.time, None)

class SwimFishProgressSync(ProgressableFishBase):
    def make_worldstepper(self):
        return iter(self.worldstep_progressive, None)

    def worldstep_progressive(self):
        part = self.amount / float(self.total)
        step = (self.actual_length + part * self.actual_length) / self.velocity
        return step

class Fish(SwimFishTimeSync, BassLook):
    """The default swimming fish, the one you very likely want to use.
    See module-level documentation.
    """

class ProgressFish(SwimFishProgressSync, BassLook):
    """A progress-based swimming fish."""

class Bird(SwimFishTimeSync, BirdLook):
    """What? A bird?"""

default_fish = Fish()
animate = default_fish.animate

fish_types = {"bass": BassLook,
              "salmon": SalmonLook,
              "bird": BirdLook,
              "duck": DuckLook}

if __name__ == "__main__":
    import signal
    import optparse
    signal.signal(signal.SIGINT, lambda *a: sys.exit(0))

    parser = optparse.OptionParser()
    parser.add_option("-f", "--fish", choices=fish_types.keys() + ["?"],
                      default="bass", help="fish type (specify ? to list)")
    parser.add_option("-v", "--velocity", type=int, default=10, metavar="V",
                      help="fish velocity (default: 10)")
    parser.add_option("--sync", choices=("none", "time"), default="time",
                      help="synchronization mechanism")

    opts, args = parser.parse_args()

    if opts.fish == "?":
        for fish_name, fish_type in fish_types.items():
            print fish_name
            print "=" * len(fish_name)
            print
            class TempFish(SwimFishTimeSync, fish_type):
                pass
            normal = TempFish().render(0, reverse=False)
            reverse = TempFish().render(0, reverse=True)
            for normline, revline in zip(normal, reverse):
                print normline, "  ", revline
            print
        sys.exit(0)
    else:
        fish_look = fish_types[opts.fish]

    if opts.sync == "time":
        fish_sync = SwimFishTimeSync
    elif opts.sync == "none":
        fish_sync = SwimFishNoSync

    class FishType(fish_sync, fish_look):
        pass

    fish = FishType()
    fish.test()
