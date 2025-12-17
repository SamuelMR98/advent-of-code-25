# Input: Single long line containing product ID ranges in the format "start-end", separated by commas
# Example: "100-200,250-300,400-500"
# Invalid IDs (made of sequence of digits repeated extrictly twice, 
# e.g., 55 '5` is repeated twice, 6464 '64' is repeated twice, 123123 '123' is repeated twice) are considered invalid.
# but 565656 is valid since '56' is repeated three times the same happens for other lengths
# IDs with leading zeros`` are also considered invalid (e.g., 00, 0101)
# Output: return the sum of all the invalid ID's that appear in the given ranges

def is_invalid_id(product_id):
    id_str = str(product_id)
    # Check for leading zeros
    if id_str[0] == '0':
        return True
    length = len(id_str)
    for sub_len in range(1, length // 2 + 1):
        if length % sub_len == 0:
            repetitions = length // sub_len
            if repetitions == 2:
                substring = id_str[:sub_len]
                if substring * repetitions == id_str:
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