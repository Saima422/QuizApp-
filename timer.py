# timer class

import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
        self._start_time = None
        self.timer_pause = []

    def start(self):            # start the timer
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()


    def pause(self):            # pause the timer
        """pause the timer and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        question_time = time.perf_counter() - sum(self.timer_pause)
        self.timer_pause.append(question_time)
        

    def stop(self):             # stop the timer
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        return elapsed_time


    def result(self):           # return the list timer_pause consisting time taken by each question
        return self.timer_pause