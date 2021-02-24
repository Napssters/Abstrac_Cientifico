#! usr/bin/env python
from Views import Landing as Ld

class Main():
    def __init__(self):
        self.LdView = Ld

    def startSummary(self):
        self.LdView.run()


if __name__ == '__main__':
    StartUp = Main()
    StartUp.startSummary()
