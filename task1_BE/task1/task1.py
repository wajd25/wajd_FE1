# def is_palindrome(s):
#     s = s.lower()   
#     is_palindrome = s == s[::-1]
#     char_frequency = {}
#     for char in s:
#         if char in char_frequency:
#             char_frequency[char] += 1
#         else:
#             char_frequency[char] = 1   
#     return is_palindrome, char_frequency

# result = is_palindrome("radar")
# print(result) 



# import math

# def is_prime(n):
#     divisors = [(n % i == 0, i) for i in range(2, int(math.sqrt(n)) + 1)]    
#     return divisors

# result = is_prime(11)
# print(result)  


import math

# Define the palindrome check function
def is_palindrome(s):
    s = s.lower()
    is_palindrome = s == s[::-1]
    char_frequency = {}
    for char in s:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return is_palindrome, char_frequency

# Define the prime check function
def is_prime(n):
    try:
        divisors = [(n % i == 0, i) for i in range(2, int(math.sqrt(n)) + 1)]
        return divisors
    except ValueError:
        return []

# Main 
def main():
    results = []
    failed_attempts = []

    # loop for the string 
    for _ in range(3):
        try:
            user_string = input("Enter a string to check if it's a palindrome: ")
            palindrome_result, char_frequency = is_palindrome(user_string)
            break
        except Exception as e:
            failed_attempts.append((user_string, str(e)))
            print(f"Invalid input. Please try again.")
    else:
        print("Max retries reached for string input.")
        return

    # loop for the numbers
    for _ in range(3):
        try:
            user_number = int(input("Enter a number to check if it's prime: "))
            prime_result = is_prime(user_number)
            break
        except ValueError as e:
            failed_attempts.append((user_number, str(e)))
            print("Invalid input. Please enter an integer.")
    else:
        print("Max retries reached for number input.")
        return

    # dictionary + add list
    result_dict = {
        "user_string": user_string,
        "palindrome_result": (palindrome_result, char_frequency),
        "user_number": user_number,
        "prime_result": prime_result
    }
    results.append(result_dict)

    # Print results
    print("\nResults:")
    print(results)

    # Print if failed 
    if failed_attempts:
        print("\nFailed Attempts:")
        print(failed_attempts)

# Run the program
if __name__ == "__main__":
    main()

