import numpy as np

FILE_SIZE_ON_GB = 2

def write_binfile(file_path = './bitfile.bin'):
    count = FILE_SIZE_ON_GB * 8 * (1024**3) // 32 
    number_array = np.random.randint(0, 2**32, count, dtype = np.uint32)
    number_array.tofile(file_path)

if __name__ == '__main__':
    write_binfile()
