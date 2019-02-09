def print_welcome_message():
    print("Welcome to stay-focused!")
    print("Hope you have some great, productive time!")


def print_help(_):
    print("work <minutes> - initializes a working session which takes exactly <minutes> minutes.")
    print("After a working session is finished, you will be notified.")
    print("break <minutes> - initializes a break which takes exaclty <minutes>")
    print("Once the break is over, you will be regularly notified that you should go back to your work " \
        "until you start a new working session.")
    print("type 'exit' to end the program.")

def bye(_):
    print("Goodbye!")
    exit(0)

def __assert_is_integer(string):
    try:
        num = int(string)
        return num
    except Exception:
        raise Exception("{} is not an integer".format(string))

def start_working_session(params):
    print("hi")
    if len(params) != 2:
        raise Exception("USAGE: work <minutes>")
    timeout = params[1]
    timeout = __assert_is_integer(timeout)
    print("done")