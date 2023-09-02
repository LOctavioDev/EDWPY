from collections import deque

#LISTAS COMO COLAS 
queue = [1, 2, 3]

queue.append(4)
queue.append(5)

queue.pop(0)
queue.pop(0)

print(queue)

#COLAS IMPLEMENTADAS EFICIENTEMENTE EN LA LIBRERIA ESTANDAR

queuee = deque([1, 2, 3])

#AGREGO LOS ELEMENTOS
queuee.append(4)
queuee.append(5)

#SACO LOS ELEMENTOS
queuee.popleft()
queuee.popleft()


print(queuee)

