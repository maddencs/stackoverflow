"""
Apparently this is called the 'Maximum Subarray' Problem. Never heard of it 
before, but here is my solution. Some guy on SO asked for help with his code, 
but it was really long and hard to read so I came up with my own solution. 
Original solution for reference: 
    https://stackoverflow.com/questions/45250185/python-maximum-subarray-sum
"""

def get_max_sum(numbers):
    start, maximum, end = 0, 0, 0
    num_len = len(numbers)
    max_list = list()
    while start <= num_len:
        count = sum(numbers[start:end])
        max_list = numbers[start:end] if count > maximum else max_list
        maximum = count if count > maximum else maximum
        end += 1
        if end >= num_len:
            start += 1
            end = start + 1
    return max_list, maximum


if __name__ == '__main__':
    numbers = [26, -25, -23, -2, 3, -6, -5, 15, 7, 8, 17, 15, 29, -2, 16, -25, -8, -25, -27, 15, -29, -11, -12, 1, -14, 21, 20, 30, -29, 17, 9, -19, 28, 11, 6, -10, -25, 27, -18, 6, -13, -13, 25, -22, 8, 9, -4, -25, 17, -26]

    print(get_max_sum(numbers))
