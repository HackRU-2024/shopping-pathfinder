import time

class Timer:
    def __init__(self):
        self.start_time = time.time()

    def elapsed_time(self):
        return self.end_time - self.start_time
    
    def __del__(self):
        self.end_time = time.time()
        print(f"Elapsed time: {self.elapsed_time()} seconds")