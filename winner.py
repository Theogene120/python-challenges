from collections import deque

def findTheWinner(n, k):
    queue = deque([n for n in range(1,n+1)])
    while len(queue) > 1:
        for i in range(1,k):
            queue.append(queue.popleft())   
        queue.popleft()
    return queue[0]        
        

print(findTheWinner(5,2))
#findTheWinner(5,2)