import time


class TooSoonError(Exception):
    # Custom exception: "TooSoonError"
    pass


def once_per_minute(f):
    '''
    Decorator function:
    Takes in a function.
    Declares a "most_recent" variable as nonlocal so it can be modified by the inner function
    '''
    most_recent = 0
    pause_time = 60

    def inside(*args, **kwargs):
        '''
        Takes in *args & **kwargs to be generic, won't actually access them.
        '''
        nonlocal most_recent

        # Stores the current time
        current_time = time.time()
        # Compares current time to the last time f was run
        if current_time - most_recent < pause_time:
            # If the time elapsed since f was last run is within the pause time then the remaining pause time is calculated
            # and declared to the user through the TooSoonError exception
            wait_until = most_recent + pause_time
            wait_time = wait_until - current_time
            raise TooSoonError(f"Wait another {wait_time} seconds")

        # Regardless of whether the above "if" statement the "most_recent" variable is adjusted with the current time
        most_recent = current_time
        # f is returned with *args & **kwargs unchanged
        return f(*args, **kwargs)
    # The decorated function is returned
    return inside


@once_per_minute
def hello(name):
    return f"Hello, {name}"


for i in range(30):
    print(i)
    try:
        time.sleep(3)
        print(hello(f"attempt {i}"))
    except TooSoonError as e:
        print(f"Too soon: {e}")