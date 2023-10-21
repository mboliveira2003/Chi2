import math
import scipy.special
import numpy as np

"""This functions convert the input data into binary format"""
def hex_to_binary(hex_string):
    # Convert a hexadecimal string to a binary string
    binary_string = bin(int(hex_string, 16))[2:]  # [2:] removes the '0b' prefix
    return binary_string

# create a function similar to the one above to convert decimal to binary
def dec_to_binary(dec_string):
    binary_string = bin(int(dec_string, 10))[2:]  # [2:] removes the '0b' prefix
    return binary_string

"""Separates string into matrices and sees if they are linearly independent"""
def matrix_test(binary_sequence, M, Q, alpha=0.01):
    # Divide the sequence into matrices of size M x Q
    N = len(binary_sequence) // (M * Q)
    binary_sequence = binary_sequence[:N * M * Q]  # Discard any unused bits
    matrices = [binary_sequence[i * M * Q: (i + 1) * M * Q] for i in range(N)]
    matrices = [np.array([int(bit) for bit in matrix]) for matrix in matrices]
                
    FM = sum(1 for matrix in matrices if np.linalg.matrix_rank(matrix.reshape(-1, Q)) == M)
    FM_minus_1 = sum(1 for matrix in matrices if np.linalg.matrix_rank(matrix.reshape(-1, Q)) == M - 1)
    remaining = N - FM - FM_minus_1

    chi_squared = (
        (FM - 0.2888 * N) ** 2 / (0.2888 * N) +
        (FM_minus_1 - 0.5776 * N) ** 2 / (0.5776 * N) +
        (remaining - 0.1336 * N) ** 2 / (0.1336 * N)
    )

    p_value = math.exp(-chi_squared / 2)

    # Test the null hypothesis
    if p_value < alpha:
        print("Reject the null hypothesis: The sequence is non-random.")
    else:
        print("Fail to reject the null hypothesis: The sequence is random.")