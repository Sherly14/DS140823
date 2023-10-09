# deque

# it is open from both the ends
# one can add/delete the elements from both the ends

from collections import deque

obj = deque([3,4,5,2,1,4,4,3,1])
print(obj)

obj.append(100)
print(obj)

obj.appendleft(200)
print(obj)

obj.pop()
print(obj)

obj.popleft()
print(obj)

obj.extend([1,2,3])
print(obj)

obj.extendleft([1,2,3])
print(obj)