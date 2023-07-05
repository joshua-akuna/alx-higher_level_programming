#!/usr/bin/python3
"""This module contains the lazy_matrix_mul function"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """The function multiplies 2 matrices using numpy"""
    return np.matmul(m_a, m_b)
