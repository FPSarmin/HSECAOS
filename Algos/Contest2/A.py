from sys import stdin


class PriorityHeap:
    def __init__(self):
        self.heap = list()

    def sift_up(self, i):
        while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:
            (self.heap[i], self.heap[(i - 1) // 2]) = (self.heap[(i - 1) // 2], self.heap[i])
            i = (i - 1) // 2

    def push(self, element):
        self.heap.append(element)
        self.sift_up(len(self.heap) - 1)

    def sift_down(self, i):
        while True:
            minpos = i
            if 2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] > self.heap[minpos]:
                minpos = 2 * i + 1
            if 2 * i + 2 < len(self.heap) and self.heap[2 * i + 2] > self.heap[minpos]:
                minpos = 2 * i + 2
            if minpos == i:
                return
            (self.heap[i], self.heap[minpos]) = (self.heap[minpos], self.heap[i])
            i = minpos

    def pop(self):
        (self.heap[0], self.heap[len(self.heap) - 1]) = (self.heap[len(self.heap) - 1], self.heap[0])
        temp = self.heap.pop()
        self.sift_down(0)
        return temp

    def get(self, i):
        return self.heap[i]


n = int(stdin.readline())
pHeap = PriorityHeap()
for i in range(n):
    temp = stdin.readline().split()
    if temp[0] == 'push':
        pHeap.push(int(temp[1]))
    if temp[0] == 'pop':
        print(pHeap.pop())
    if temp[0] == 'get':
        print(pHeap.get(int(temp[1])))
