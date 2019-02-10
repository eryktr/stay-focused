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

    def start_working_session(self, params):
        interface = self.interface
        if len(params) != 2:
            raise Exception("USAGE: work <minutes>")
        timeout = params[1]
        timeout = self.__assert_is_integer(timeout)
        interface.work_timer.set_timeout(timeout)
        interface.work_timer.run()

