import conf


def run():
    print conf.get('IP')
    conf.set('IP', 20)