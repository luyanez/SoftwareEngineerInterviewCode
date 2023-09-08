from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        self.size = size
        self.queue = deque()
        # number of elements seen so far
        self.window_sum = 0
        self.count = 0
    
    def next(self, val):
        self.count += 1
        # calculate the new sum by shifting the window
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0
        self.window_sum = self.window_sum - tail + val

        return self.window_sum / min(self.size, self.count)

# input
# ['MovingAverage', "next", "next", "next", "next"]
# [3, 1, 10, 3, 5]
#obj = MovingAverage(size)
#param1 = obj.next(val)