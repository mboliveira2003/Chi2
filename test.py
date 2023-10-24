# Import packages

import numpy
import requests
from nistrng import check_eligibility_all_battery, run_all_battery, SP800_22R1A_BATTERY

def get_generated_numbers(count, bits):
    # Define the API endpoint
    api_url = 'https://noisr-api.onrender.com/generate'
    
    # Define the request payload (number of numbers and number of bits)
    payload = {
        'count': count,
        'bits': bits,
    }
    
    try:
        # Send a POST request to the API
        response = requests.post(api_url, json=payload)
        response.raise_for_status()  # Raise an exception for any HTTP error
        data = response.json()
        generated_numbers = data['numbers']
        return generated_numbers
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    
# Function that coverts a binary string to a decimal string
def binary_to_decimal(binary_string):
    # Convert a binary string to a decimal string
    decimal_string = str(int(binary_string, 2))
    return decimal_string


if __name__ == "__main__":

    # Generate a sequence of 4 numbers of 4 bits each
    count = 10
    bits = 8
    generated_numbers = get_generated_numbers(count, bits)
    
    binary_sequence = []
    decimal_sequence = []
    if generated_numbers:
        print("Generated Numbers:")
        for num in generated_numbers:
            decimal_sequence += [int(str(int(num, 2)))]
            for bit in num:
                binary_sequence += [int(bit)]
    else:
        print("Failed to retrieve generated numbers.")

    print(decimal_sequence)
    print(binary_sequence)
    binary_sequence: numpy.array = numpy.array(binary_sequence)

    # Check the eligibility of the test and generate an eligible battery from the default NIST-sp800-22r1a battery
    eligible_battery: dict = check_eligibility_all_battery(binary_sequence, SP800_22R1A_BATTERY)
    # Print the eligible tests
    print("Eligible test from NIST-SP800-22r1a:")
    for name in eligible_battery.keys():
        print("-" + name)

    # Test the sequence on the eligible tests
    results = run_all_battery(binary_sequence, eligible_battery, False)

    # Print results one by one
    print("Test results:")
    for result, elapsed_time in results:
        if result.passed:
            print("- PASSED - Score: " + str(result.score) + " - " + result.name + " - elapsed time: " + str(elapsed_time) + " ms")
        else:
            print("- FAILED - Score: " + str(result.score) + " - " + result.name + " - elapsed time: " + str(elapsed_time) + " ms")

    # Make a histogram with the generated sequence
    import matplotlib.pyplot as plt
    plt.hist(decimal_sequence, bins=10)
    plt.show()
