import math
import scipy.stats as stats
import scipy.special

"""Funtions to convert input data into binary format"""
def hex_to_binary(hex_string):
    # Convert a hexadecimal string tso a binary string
    binary_string = bin(int(hex_string, 16))[2:]  # [2:] removes the '0b' prefix
    return binary_string

def dec_to_binary(dec_string):
    binary_string = bin(int(dec_string, 10))[2:]  # [2:] removes the '0b' prefix
    return binary_string

"""Tests if occurence of sequences of repeated 1s and 0s are as frequent as expected"""
def runs_test(binary_sequence, alpha=0.01):
    n = len(binary_sequence) 
    
    # Calculate the proportion π of ones in the input sequence
    ones_count = binary_sequence.count('1')
    pi = ones_count / n
    
    # Determine if the prerequisite Frequency (Monobit) test is passed
    tau = 2 / math.sqrt(n)
    if abs(pi - 0.5) >= tau:
        # The prerequisite Frequency test is not passed, test is not applicable
        return 0.0

    # Compute the test statistic V(obs)
    runs = [0]  # Initialize with a run of 0
    for i in range(1, n):
        if binary_sequence[i] != binary_sequence[i - 1]:
            runs.append(1)
        else:
            runs.append(0)
    v_obs = sum(runs) + 1 
    
    # Compute the P-value
    p_value = scipy.special.erfc(abs(v_obs - 2 * n * pi * (1 - pi)) / (2 * math.sqrt(2 * n) * pi * (1 - pi)))

    # Check if the null hypothesis is rejected
    if p_value < alpha:
        print("Reject the null hypothesis: The sequence is non-random.")
    else:
        print("Fail to reject the null hypothesis: The sequence is random.")