from threading import Timer
from time import sleep

import conf
import tmp2


if __name__ == "__main__":
    #conf.init()
    conf.set('IP', 10)
    print conf.get('IP')

    x = Timer(1, tmp2.run)
    x.start()
    sleep(2)
    print conf.get('IP')