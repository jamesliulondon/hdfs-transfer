from datetime import datetime, timedelta

class Rtime:

    def today(self, d=0):
        """
        microseconds
        """
        return datetime.now() + timedelta (days=d)

    def reverse_short(self,inputtime):
        return inputtime.strftime('%Y%m%d')

