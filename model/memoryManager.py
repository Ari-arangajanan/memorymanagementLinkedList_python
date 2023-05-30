from model.Memory import Memory


class MemoryManager:
    def __init__(self):
        self.free_memory = None
        self.memory_size = None
        self.osAllocation = None

    def node(self, memory_size, os_allocation):
        self.memory_size = memory_size
        self.osAllocation = os_allocation
        self.free_memory = Memory((memory_size - os_allocation), os_allocation)
        print("Memory is allocated: from main class")

    def allocate_memory(self, process_id, size):
        current_free_memory = self.free_memory
        previous_memory = None

        while current_free_memory:
            if not current_free_memory.process_id and current_free_memory.size >= size:
                allocated_memory = Memory(current_free_memory.start_address, size)
                allocated_memory.process_id = process_id
                allocated_memory.next_block = current_free_memory.next_block
                allocated_memory.start_address += size
                allocated_memory.size = size
                allocated_memory.next_block = allocated_memory
                return True
            previous_memory = current_free_memory
            current_free_memory = current_free_memory.next_block
            print("tttttttttttttttttttttttty", current_free_memory)
            return False

    def release_memory(self, process_id):
        current_free_memory = self.free_memory

        while current_free_memory:
            if current_free_memory.process_id == process_id:
                current_free_memory.process_id = None

                # Merge the spaces
                if current_free_memory.next_block and not current_free_memory.next_block.process_id:
                    current_free_memory.size += current_free_memory.next_block.size
                    current_free_memory.next_block = current_free_memory.next_block.next_block

                if previous_memory and not previous_memory.process_id:
                    previous_memory.size += current_free_memory.size
                    previous_memory.next_block = current_free_memory.next_block
                    print("eeeeeeeeeeeeee", previous_memory.next_block)
                return True

            previous_memory = current_free_memory
            current_free_memory = current_free_memory.next_block
            print("taaaaaaaaaaaaaaaaaa", current_free_memory)
        return False

    def snapshot(self):
        print("Memory Snapshot:")
        current_free_memory = self.free_memory
        while current_free_memory:
            status = "Free" if not current_free_memory.process_id else f"Allocated to P{current_free_memory.process_id}"
            print(
                f"Address: {current_free_memory.start_address} - {current_free_memory.start_address + current_free_memory.size - 1} ({status})")
            current_free_memory = current_free_memory.next_block

        '''while current_free_memory:'''
