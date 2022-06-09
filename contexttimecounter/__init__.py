__version__ = '0.1.0'

import time

class ContextTimeCounter:
    """
    A little context time counter.
    Use it as:
    ```py
    with ContextTimeCounter() as ctc:
        # ...
    print(f"Time spent in the context: {ctc.time_total:.4f}")
    ```
    """

    def __enter__(self):
        self.begin_time = time.perf_counter()
        return self
    
    def __exit__(self, exception_type, exception_value, traceback):
        self.end_time = time.perf_counter()

    @property
    def time_now(self):
        """
        :returns: Delta [in seconds] since entering the context.
        """
        return (time.perf_counter() - self.begin_time)

    @property
    def time_total(self) -> float:
        """
        Can only be used after the context has been exited.

        :returns: Total time [in seconds] between entering and exiting the context.
        """
        return self.end_time - self.begin_time
