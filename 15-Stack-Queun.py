# Stack (LIFO:Last-In-First-Out)

Cars = []

Cars.append("A")
Cars.append("B")
Cars.append("C")
Cars.append("D")

# print (Cars)        # ['A', 'B', 'C', 'D']
# print (Cars[-1])    # D
# Cars.pop()          # ['A', 'B', 'C', 'D'] - 'D'
# print (Cars)        # ['A', 'B', 'C']

# Queue (FIFO:First-In-First-Out)

from collections import deque


Cars = deque([])

Cars.append("A")
Cars.append("B")
Cars.append("C")
Cars.append("D")

print (Cars)            # deque(['A', 'B', 'C', 'D'])
print (Cars[0])         # A
if Cars:
    Cars.popleft()      # ['A', 'B', 'C', 'D'] - 'A'
    print (Cars)        # deque(['B', 'C', 'D'])
if not Cars:
    print("no data for output")