# Input: Single long line containing product ID ranges in the format "start-end", separated by commas
# Example: "100-200,250-300,400-500"
# An ID is invalid if it is made only of some sequence of digits repeated at least twice.
# So, 12341234 (1234 repeated twice) is invalid, 123123123 (123 repeated three times) is invalid,
# 12121212 (12 repeated four times) is invalid, etc.
# Output: return the sum of all the invalid ID's that appear in the given ranges

def is_invalid_id(product_id):
    id_str = str(product_id)
    length = len(id_str)
    # Check for repeated sequences
    for i in range(1, length // 2 + 1):
        if length % i == 0:
            if id_str == id_str[:i] * (length // i):
                return True
    return False

def sum_invalid_ids(ranges):
    total_invalid_sum = 0

    for r in ranges:
        start, end = map(int, r.split('-'))
        for product_id in range(start, end + 1):
            if is_invalid_id(product_id):
                # print(f"Invalid ID found: {product_id}")
                total_invalid_sum += product_id

    return total_invalid_sum

if __name__ == "__main__":
    # get ranges from day2_input.txt
    with open("day2_input.txt", "r") as file:
        line = file.readline().strip()
        ranges = line.split(',')
    result = sum_invalid_ids(ranges)
    print(f"The sum of all invalid product IDs: {result}")