def reverse(self):
    prev = None
    current = self.head
    while (current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    self.head = prev