__author__ = 'masted'


class Service:

    def __init__(self):
        pass

    def is_up(self):
        return False

    def is_down(self):
        return not self.is_up()


class StatusSite:

    def __init__(self):
        pass

    def in_state(self, state):
        pass

    def to_state(self, state):
        pass
