class Queue:

    def __init__(self):
        self.queue = []
        self.size = 0

    #Element addition
    def enqueue(self, item):
        self.queue.append(item)
        self.size += 1

    #Element remove
    def dequeue(self):
        if len(self.queue)<1:
            return None

        self.size -= 1
        return self.queue.pop()

    #for print
    def Print(self):
        print(self.queue)


if __name__ == '__main__':

    info = Queue()
    info.enqueue(1)
    info.enqueue(2)
    info.enqueue(3)
    info.enqueue(4)
    info.enqueue(5)

    info.Print()

    info.dequeue()
    info.dequeue()

    print("\nAfter removing elements:\n")
    info.Print()
    print("\nQueue size:")
    print(info.size)
