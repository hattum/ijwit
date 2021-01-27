import heapq

class PriorityQueue:
    def __init__(self):
        self._elements = []

    def put(self, item, priority):
        heapq.heappush(self._elements, (priority, item))

    def get(self):
        return heapq.heappop(self._elements)[1]

    def getpriority(self):
        return (self._elements)[0][0]

    def is_empty(self):
        return len(self._elements) == 0

    def qsize(self):
        return len(self._elements)

    def description(self):
        if self._elements:
            return f"Lengte van de PriorityQueue is {len(self._elements)}"
        return f"The list is empty"

    def smallests(self, n): 
        self._elements = heapq.heapify(heapq.nsmallest(n, self._elements))

