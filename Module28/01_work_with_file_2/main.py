class File:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        
    def __enter__(self):
        try:
            self.file = open(self.file_name, self.mode)
        except FileNotFoundError:
            self.file = open(self.file_name, 'w')
        finally:
            return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True
    
    def write(self, date):
        self.file.write(date)
        

with File('file_txt.txt', 'r') as my_file:
    my_file.write('Hello!')
