import os
import csv

class CsvStore:
    def __init__(self, path, headers):
        self.path = os.path.join(os.getcwd(), path)
        self.headers = headers
    
    def read(self):
        with open(self.path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                data.append(dict(row))
            return data
    
    def flush(self, data):
        with open(self.path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(self.headers)
            for item in data:
                writer.writerow(item.values())