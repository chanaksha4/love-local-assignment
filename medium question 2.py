# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
def majority_elements(nums):
    if not nums:
        return []

    candidate1, count1 = None, 0
    candidate2, count2 = None, 0

    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
            
    result = []
    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3:
        result.append(candidate2)

    return result

# example usage
nums1 = [3, 2, 3]
print(majority_elements(nums1))  # Output: [3]

nums2 = [1]
print(majority_elements(nums2))  # Output: [1]

nums3 = [1, 2]
print(majority_elements(nums3))  # Output: [1, 2]


# Take user input
user_input = input("Enter integers separated by spaces: ")
nums = list(map(int, user_input.split()))

# Call the function and print the result
result = majority_elements(nums)
print(f"Elements appearing more than ⌊ n/3 ⌋ times: {result}")


