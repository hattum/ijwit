import heapq

class PriorityQueue:
    def __init__(self):
        self._elements = []

    def put(self, item, priority):
        heapq.heappush(self._elements, (priority, item))

    def get(self):
        return heapq.heappop(self._elements)[1]

    def getter(self):
        return (self._elements)[0][0]

    def is_empty(self):
        return len(self._elements) == 0

    def description(self):
        if self._elements:
            return f"lengte is {len(self._elements)}"
        return f"The list is empty"

def main():

    pq = PriorityQueue()
    print(pq)
    print(pq.is_empty())

    # item, priority
    pq.put("whatever", 2)
    pq.put("joehoe!", 1)
    pq.put("sleeplekker", 3)

    print(pq)

    print(pq.getter())
    print(pq.get())
    print(pq.getter())
    print(pq.get())
    print(pq.getter())
    print(pq.get())


    print(pq)

if __name__ == "__main__":
    main()