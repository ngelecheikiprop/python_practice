#!/usr/bin/python3
from collections import deque
queue = deque(['Kiprop' , 'Chem', 'Kibet'])
queue.append('Schola')#schola arrives
queue.append('ngosh')#ngosh arrives
queue.append('kiptum')#kiptum arrives
print(queue)
queue.popleft()
print(queue)
print("kiprop left first")
