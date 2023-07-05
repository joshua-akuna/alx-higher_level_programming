#!/usr/bin/python3
import numpy as np
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul
if __name__ == '__main__':
    print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
