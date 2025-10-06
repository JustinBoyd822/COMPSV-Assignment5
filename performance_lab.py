# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3
def most_frequent(numbers):
    if not numbers:
        return None
    
    freq = {}
    max_count = 0
    most_freq = None
    
    # Single pass: count and track max simultaneously
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > max_count:
            max_count = freq[num]
            most_freq = num
    
    return most_freq

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) - still need to count all elements
- Worst-case: O(n) - single pass through all n elements
- Average-case: O(n) - linear scan is required regardless
- Space complexity: O(k) where k is number of unique elements, worst case O(n) if all unique
- Why this approach? Hash map provides O(1) lookup/update for counting frequencies.
  Single-pass optimization tracks maximum while counting.
- Could it be optimized? Could use Counter from collections for cleaner code, but same O(n) complexity.
"""

# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]
def remove_duplicates(nums):
    if not nums:
        return []
    
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

"""
Time and Space Analysis for problem 2:
- Best-case: O(n) - must check every element even if all unique
- Worst-case: O(n) - single pass through all elements
- Average-case: O(n) - linear time regardless of duplicates
- Space complexity: O(n) - seen set can hold up to n unique elements, result list up to n elements
- Why this approach? Set provides O(1) average lookup to track seen elements while preserving order.
  Alternative approaches like nested loops would be O(n²).
- Could it be optimized? This is optimal for preserving order. Could use dict.fromkeys(nums) 
  in Python 3.7+ (preserves insertion order), but same complexity.
"""

# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]
def find_pairs(nums, target):
    if not nums:
        return []
    
    seen = set()
    pairs = []
    
    for num in nums:
        complement = target - num
        if complement in seen:
            # Use tuple with smaller element first for consistency
            pair = (min(num, complement), max(num, complement))
            pairs.append(pair)
        seen.add(num)
    
    return pairs

"""
Time and Space Analysis for problem 3:
- Best-case: O(n) - must check all elements even if no pairs exist
- Worst-case: O(n) - single pass with O(1) set operations
- Average-case: O(n) - linear time complexity
- Space complexity: O(n) - seen set stores up to n elements, pairs list stores up to n/2 pairs
- Why this approach? Single-pass with set lookup avoids nested loops. By checking if complement 
  exists in previously seen elements, we find all pairs efficiently without duplicates.
- Could it be optimized? This is optimal at O(n). Alternative sorting approach would be O(n log n).
"""

# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.
def add_n_items(n):
    capacity = 1
    size = 0
    storage = [None] * capacity
    
    for i in range(n):
        # Check if resize needed
        if size == capacity:
            old_capacity = capacity
            capacity *= 2
            print(f"Resizing from {old_capacity} to {capacity}")
            
            # Simulate copying to new array
            new_storage = [None] * capacity
            for j in range(size):
                new_storage[j] = storage[j]
            storage = new_storage
        
        # Add the item
        storage[size] = i
        size += 1
        print(f"Added item {i}, size now {size}/{capacity}")

"""
Time and Space Analysis for problem 4:
- When do resizes happen? When size equals capacity (at sizes 1, 2, 4, 8, 16, ...)
  This occurs log₂(n) times for n insertions.
- What is the worst-case for a single append? O(n) - when resize occurs, must copy all n elements
- What is the amortized time per append overall? O(1) amortized
  Proof: Resizes cost 1 + 2 + 4 + 8 + ... + n ≈ 2n total operations for n inserts.
  So n appends cost approximately 3n operations total → O(1) amortized per append.
- Space complexity: O(n) - array holds n elements with some unused capacity
- Why does doubling reduce the cost overall? Doubling means we resize only log(n) times instead 
  of n times (which would happen if we increased by a constant). The geometric series 
  1+2+4+...+n sums to approximately 2n, making the total cost linear rather than quadratic.
  Each doubling "pays forward" for many future insertions without resizing.
"""

# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]
def running_total(nums):
    if not nums:
        return []
    
    result = []
    total = 0
    
    for num in nums:
        total += num
        result.append(total)
    
    return result

"""
Time and Space Analysis for problem 5:
- Best-case: O(n) - must process every element
- Worst-case: O(n) - single pass through all elements
- Average-case: O(n) - linear time always
- Space complexity: O(n) - result list stores n elements (O(1) auxiliary space if not counting output)
- Why this approach? Single pass with running sum is most efficient. Each element 
  processed exactly once, avoiding redundant re-summation. Naive approach of summing 
  nums[0:i+1] for each index i would be O(n²).
- Could it be optimized? This is optimal at O(n). Python's itertools.accumulate() implements 
  this same algorithm. Cannot do better than linear since we must examine each element.
"""
- Why this approach?
- Could it be optimized?
"""
