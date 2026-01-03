import csv
import os

class FileHandling:   
    def __init__(self):
        self._filename = "data.csv" 

    def create_file(self):
        with open(self._filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Time", "CPU", "GPU Temp", "GPU", "RAM"])
            writer.writeheader()
    
    def add_data(self, cpu_u, gpu_u, ram_u, time_u):
        with open(self._filename, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Time", "CPU", "GPU Temp", "GPU", "RAM"])
            writer.writerow({
                "Time": time_u,
                "CPU": cpu_u,
                "GPU Temp": gpu_u["temp"],
                "GPU": gpu_u["mem"],
                "RAM": ram_u
                })
            
    def delete_file(self):
        if os.path.exists(self._filename):
            os.remove(self._filename)

    

