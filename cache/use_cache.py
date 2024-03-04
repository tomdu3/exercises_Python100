#
# www.youtube.com/@indently
#

import time
from functools import cache


@cache  # takes result from the cache if the same arguments are used for a call
def calc(x):
    print(f'{x} + 1 is ...')
    time.sleep(2)
    return x + 1


while True:
    input_ = int(input('>> '))
    print(calc(input_))
