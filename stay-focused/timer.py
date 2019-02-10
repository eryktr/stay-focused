import time
import abc

#timeout in minutes
class Timer(abc.ABC):
    @abc.abstractmethod
    def inform(self):
        pass

    @abc.abstractmethod
    def alert(self):
        pass

    def __init__(self, interface):
        self.timeout = 0
        self.interface = interface
    
    def set_timeout(self, timeout):
        self.timeout = timeout

    def tick(self):
        self.timeout -= 1
        self.inform()
    
    def is_not_up(self):
        return self.timeout > 0

    def run(self):
        while self.is_not_up():
            time.sleep(60)
            self.tick()
        self.alert()

class WorkTimer(Timer):
    def __init__(self, interface):
        super().__init__(interface)

    def alert(self):
        self.interface.write_line("Work done", True)
        time.sleep(1)
        self.interface.show_info_alert("Done!", "Congratulations! Your work session has been finished.")

    def inform(self):
        msg = "Remaining work time: {} {}".format(self.timeout, "minutes" if self.timeout > 1 else "minute")
        self.interface.write_line(msg , True)

        
class BreakTimer(Timer):
    def __init__(self, interface):
        super().__init__(interface)

    def alert(self):
        self.interface.write_line("Break over!", True)
        self.interface.show_warning_alert("Break over!", "Break over! Get back to work!")

    def inform(self):
        msg = "Remaining break time: {} {}".format(self.timeout, "minutes" if self.timeout > 1 else "minute")
        self.interface.write_line(msg, True)