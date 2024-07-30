from collections import deque

queue = deque([1, 2, 3, 4, 5])

queue.append(6)
queue.append(7)

queue.popleft()  # pop from the left. First in First out
queue.popleft()  # Output: deque([3, 4, 5, 6, 7])


print(queue)

print(id(queue[3]))

