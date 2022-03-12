import contextlib
import cProfile
import os

@contextlib.contextmanager
def profile(filename='profile.prof', *kargs, **kwargs):
    profile = cProfile.Profile(*kargs, **kwargs)

    profile.enable()
    yield
    profile.disable()

    if filename:
        profile.dump_stats(os.path.expanduser(filename))

    else:
        profile.print_stats()


################################################################################
# Tests

import tempfile
import random 

with tempfile.TemporaryDirectory() as tmpdirname:
    with profile(filename=os.path.join(tmpdirname, "profile.prof")):
        x = 0

        for _ in range(100000): 
             x += random.randint(-5, 5)

