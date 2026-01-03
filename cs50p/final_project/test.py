import multiprocessing

def stress_cpu():
    while True:
        _ = 23948230948 ** 234092834

if __name__ == "__main__":
    # Create one process per CPU core to maximize usage
    processes = []
    for _ in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=stress_cpu)
        p.start()
        processes.append(p)
    
    input("Press Enter to stop CPU stress test...")
    for p in processes:
        p.terminate()