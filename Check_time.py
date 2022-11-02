from datetime import datetime

class checktime:
    def __init__(self):

        self.now = datetime.now()
        self.w = self.now.weekday()+1
        self.h = self.now.hour
        self.m = self.now.minute

        if self.w == 3 and self.h == 23 and self.m == 54:
            print('jopa')