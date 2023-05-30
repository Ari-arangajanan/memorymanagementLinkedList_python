class Memory:
    def __init__(self, address, size):
        self.start_address = address
        self.size = size
        self.process_id = None
        self.next_block = None

