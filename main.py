from model.memoryManager import MemoryManager

if __name__ == "__main__":
    MemoryManager = MemoryManager()
    MemoryManager.node(2560,600)

    MemoryManager.allocate_memory("p1",600)
    MemoryManager.allocate_memory("p2", 1000)
    MemoryManager.allocate_memory("p3", 300)

    MemoryManager.release_memory("p1")

    MemoryManager.allocate_memory("p4",700)

    MemoryManager.allocate_memory("p3", 1000)

    MemoryManager.snapshot()


