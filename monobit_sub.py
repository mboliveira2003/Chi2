from scipy.stats import chisquare
import numpy as np
import math
import scipy.special

"""This functions convert the input data into binary format"""
def hex_to_binary(hex_string):
    # Convert a hexadecimal string to a binary string
    binary_string = bin(int(hex_string, 16))[2:]  # [2:] removes the '0b' prefix
    return binary_string

def dec_to_binary(dec_string):
    # Convert a decimal string to a binary string
    binary_string = bin(int(dec_string, 10))[2:]  # [2:] removes the '0b' prefix
    return binary_string

"""Tests if occurence of 1s and 0s within blocks of the sequence is random"""
def monobit_sub_test(binary_sequence, M, alpha=0.01):
    # Splitting the sequence into blocks
    N = len(binary_sequence) // M
    binary_sequence = binary_sequence[:N * M]  # Discard any unused bits
    blocks = [binary_sequence[i * M: (i + 1) * M] for i in range(N)]

    # Calculate proportions of ones in each block
    proportions = [block.count('1') / len(block) for block in blocks]

    # Compute the test statistic
    chi_squared = 4 * M * sum((pi - 0.5) ** 2 for pi in proportions)
    p_value = scipy.special.gamc(N / 2, chi_squared / 2)

    # Test the null hypothesis
    if p_value < alpha:
        print("Reject the null hypothesis: The sequence is non-random.")
    else:
        print("Fail to reject the null hypothesis: The sequence is random.")

