import collections
queue = collections.deque()


queue = collections.deque([1,2,3])

queue.append(4)
queue.append(5)

queue.popleft() #1
queue.popleft() #2

queue[0]  #3

len(queue)  #3