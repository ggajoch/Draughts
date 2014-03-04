import ConfigParser
import os

file = os.path.dirname(__file__) + '/conf.cfg'

config = ConfigParser.RawConfigParser()
config.readfp(open(file))


def get(variable):
    return config.get('1', variable)


def set(variable, value):
    config.set('1', variable, value)


def save_config():
    try:
        with open(file, 'wb') as configfile:
            config.write(configfile)
    except:
        print "Cannot write config file!"


def build_default_config():
    config = ConfigParser.RawConfigParser()
    config.read('conf.cfg')
    config.set('1', 'IP', '192.168.1.101')
    config.set('1', 'threshold', 400)
    #...............
    try:
        with open(file, 'wb') as configfile:
            config.write(configfile)
    except:
        print "Cannot write config file!"


if __name__ == "__main__":
    print os.path.dirname(__file__) + '/conf.cfg'
    print get('IP')
    set('IP', 192)

    print get('IP')
"""    print get('IP')
    set('IP',"192.168.1.101")
    print get('IP')

    print get('threshold')
    set('threshold',200)
    print get('threshold')"""
