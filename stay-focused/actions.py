import time
import threading
import multiprocessing
class ActionPerformer():

    def __init__(self, interface):
        self.interface = interface

    def print_welcome_message(self):
        interface = self.interface
        interface.write_line("Welcome to stay-focused!")
        interface.write_line("Hope you have some great, productive time!")

    def print_help(self, _):
        interface = self.interface
        interface.write_line("work <minutes> - initializes a working session which takes exactly <minutes> minutes.")
        interface.write_line("After a working session is finished, you will be notified.")
        interface.write_line("break <minutes> - initializes a break which takes exaclty <minutes>")
        interface.write_line("Once the break is over, you will be regularly notified that you should go back to your work " \
            "until you start a new working session.")
        interface.write_line("type 'exit' to end the program.")

    def bye(self, _):
        self.interface.write_line("Goodbye!")
        exit(0)

    def __assert_is_integer(self, string):
        try:
            num = int(string)
            return num
        except Exception:
            raise Exception("{} is not an integer".format(string))

    def __assert_params_are_correct(self, params):
        if len(params) != 2:
            raise Exception("USAGE: work <minutes>")

    def __get_timeout(self, params):
        timeout = params[1]
        timeout = self.__assert_is_integer(timeout)
        return timeout

    def start_working_session(self, params):
        interface = self.interface
        self.__assert_params_are_correct(params)
        timeout = self.__get_timeout(params)
        interface.work_timer.set_timeout(timeout)
        interface.work_timer.run()

    def start_break(self, params):

        def make_hell_from_life():
            interface = self.interface
            while interface.work_timer.timeout == 0:
                interface.show_warning_alert("GO BACK!", "BACK TO WORK, NOW!")
                time.sleep(10)
            
        interface = self.interface
        self.__assert_params_are_correct(params)
        timeout = self.__get_timeout(params)
        interface.break_timer.set_timeout(timeout)
        interface.break_timer.run()
        t = threading.Thread(target=make_hell_from_life)
        t.start()
        return
