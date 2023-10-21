from scipy.stats import chisquare
import math
import scipy.special

"""This functions convert the input data into binary format"""
def hex_to_binary(hex_string):
    # Convert a hexadecimal string to a binary string
    binary_string = bin(int(hex_string, 16))[2:]  # [2:] removes the '0b' prefix
    return binary_string

# create a function similar to the one above to convert decimal to binary
def dec_to_binary(dec_string):
    binary_string = bin(int(dec_string, 10))[2:]  # [2:] removes the '0b' prefix
    return binary_string

"""Tests if 1s and 0s are equally likely to occur in the sequence"""
def monobit_test(binary_sequence, alpha=0.01):
    # Convert binary sequence to ±1
    pm1_sequence = [2 * int(bit) - 1 for bit in binary_sequence]

    # Compute test statistic
    sobs = sum(pm1_sequence) / math.sqrt(len(binary_sequence))

    # Compute P-value
    p_value = scipy.special.erfc(abs(sobs) / math.sqrt(2))

    # Check if the null hypothesis is rejected
    if p_value < alpha:
        print("Reject the null hypothesis: The sequence is non-random.")
    else:
        print("Fail to reject the null hypothesis: The sequence is random.")
































def convert_binary_to_pm1(binary_sequence):
    return [2 * int(bit) - 1 for bit in binary_sequence]

def calculate_sobs(sequence):





























    n = len(sequence)
    return sum(sequence) / math.sqrt(n)

def calculate_p_value(sobs):
    return 0.5 * scipy.special.erfc(sobs / math.sqrt(2))

# Example binary sequence
binary_sequence = "1011010101"

# Step 1: Convert binary sequence to ±1
pm1_sequence = convert_binary_to_pm1(binary_sequence)

# Step 2: Calculate sobs
sobs = calculate_sobs(pm1_sequence)

# Step 3: Calculate the P-value
p_value = calculate_p_value(sobs)

print(f"Binary Sequence: {binary_sequence}")
print(f"±1 Sequence: {pm1_sequence}")
print(f"sobs: {sobs:.9f}")
print(f"P-value: {p_value:.6f}")
