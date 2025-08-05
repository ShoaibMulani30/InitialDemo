def distinct_letters(s):
    return set(filter(str.isalpha, s))

# Example usage
input_str = "Hello, World!"
print(distinct_letters(input_str))