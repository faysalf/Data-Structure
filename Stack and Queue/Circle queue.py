class CircularQueue:

    def __init__(self, maxSizeQ):
        self.queue = [0] * maxSizeQ

        self.max_size = maxSizeQ
        self.head = 0
        self.tail = 0
        self.size = 0



    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size


    def enQueue(self, item):
        if self.isFull():
            return 'Queue is Full!'

        else:

            #add element
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1


    def deQueue(self):
        if self.isEmpty():
            return 'Queue is Empty!'

        else:

            # fetch data
            data = self.queue[self.head]
            # increment head
            self.head = (self.head + 1) % self.max_size
            self.size -= 1

            return data


if __name__ == '__main__':
    q_size = 5
    q = CircularQueue(q_size)

    q.enQueue('Faysal')
    q.enQueue(165091)
    q.enQueue("GPA: 3.86")
    q.enQueue("Jobayer")
    q.enQueue("Yasin")


    print('Before Queue:')
    for i in q.queue:
        print(i)

    q.deQueue()
    q.deQueue()

    print('\nAfter dequeue:')
    while not q.isEmpty():
        person = q.deQueue()
        print(person)
