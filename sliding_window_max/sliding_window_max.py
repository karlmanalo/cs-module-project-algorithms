'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    
    sliding_max = []

    # Iterating over range of number of windows that exist in the array given k
    for i in range(len(nums) - (k - 1)):
        # Appending maximum value of each window to sliding_max
        sliding_max.append(max(nums[i: i + k]))
    return sliding_max

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
