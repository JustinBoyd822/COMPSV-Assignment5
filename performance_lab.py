# Assignment #5: Test, Analyze, Optimize
# Performance Lab - Algorithm Analysis

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
  This single-pass approach is already optimized compared to a two-pass solution.
- Trade-offs: Uses O(k) extra space for hash map. Could use sorting O(n log n) with O(1) extra space,
  but that would be slower.
"""

# Test cases for Problem 1
def test_most_frequent():
    # Basic case
    assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
    # Single element
    assert most_frequent([5]) == 5
    # All same
    assert most_frequent([2, 2, 2, 2]) == 2
    # Empty list
    assert most_frequent([]) == None
    # Two elements tie
    result = most_frequent([1, 1, 2, 2])
    assert result in [1, 2]
    # Negative numbers
    assert most_frequent([-1, -1, -2, -3, -1]) == -1
    print("✅ All tests passed for most_frequent!")

test_most_frequent()


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

# ORIGINAL SOLUTION (kept for comparison):
def remove_duplicates_original(nums):
    """Original O(n) time, O(n) space solution"""
    if not nums:
        return []
    
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# OPTIMIZED SOLUTION:
def remove_duplicates(nums):
    """
    OPTIMIZATION EXPLANATION:
    This optimized version uses dict.fromkeys() which:
    1. Preserves insertion order (Python 3.7+)
    2. Automatically handles duplicates
    3. Reduces code complexity while maintaining O(n) time
    4. Uses slightly less memory overhead than separate set + list
    
    Performance comparison to original:
    - Time: Same O(n) but fewer operations (single dict construction vs loop + conditionals)
    - Space: Same O(n) but marginally better (one dict vs set + list)
    - Code: Cleaner, more Pythonic, less error-prone
    
    Trade-off: Relies on Python 3.7+ dict ordering guarantee
    """
    if not nums:
        return []
    return list(dict.fromkeys(nums))

"""
Time and Space Analysis for problem 2:
- Best-case: O(n) - must check every element even if all unique
- Worst-case: O(n) - single pass through all elements
- Average-case: O(n) - linear time regardless of duplicates
- Space complexity: O(n) - dict can hold up to n unique elements
- Why this approach? dict.fromkeys() leverages Python's ordered dict to efficiently
  remove duplicates while preserving order in a single operation.
- Could it be optimized? This is optimal for preserving order at O(n) time.
  Cannot do better than O(n) since we must examine each element.
- Trade-offs: Requires Python 3.7+. Original set-based approach is more explicit
  and works in older Python versions.
"""

# Test cases for Problem 2
def test_remove_duplicates():
    # Basic case
    assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
    # No duplicates
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    # All duplicates
    assert remove_duplicates([1, 1, 1, 1]) == [1]
    # Empty list
    assert remove_duplicates([]) == []
    # Single element
    assert remove_duplicates([42]) == [42]
    # Order preservation test
    assert remove_duplicates([3, 1, 2, 3, 1]) == [3, 1, 2]
    # Negative and zero
    assert remove_duplicates([0, -1, 0, -1, 5]) == [0, -1, 5]
    print("✅ All tests passed for remove_duplicates!")

test_remove_duplicates()


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
- Trade-offs: Uses O(n) extra space. Could sort and use two pointers for O(1) extra space
  but O(n log n) time. Current approach prioritizes speed over space.
"""

# Test cases for Problem 3
def test_find_pairs():
    # Basic case
    result = find_pairs([1, 2, 3, 4], 5)
    assert set(result) == {(1, 4), (2, 3)}
    # No pairs
    assert find_pairs([1, 2, 3], 10) == []
    # Empty list
    assert find_pairs([], 5) == []
    # Single element
    assert find_pairs([5], 10) == []
    # Pair with zero
    assert find_pairs([0, 5, -5, 3], 0) == [(-5, 5)]
    # Multiple pairs
    result = find_pairs([1, 2, 3, 4, 5, 6], 7)
    assert set(result) == {(1, 6), (2, 5), (3, 4)}
    # Negative numbers
    result = find_pairs([-1, -2, 3, 4], 2)
    assert set(result) == {(-2, 4), (-1, 3)}
    print("✅ All tests passed for find_pairs!")

test_find_pairs()


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
- Trade-offs: Uses extra space (up to 2x needed). Alternative: grow by fixed amount (e.g., +10)
  would use less space but resize more often, resulting in O(n²) total time for n insertions.
"""

# Test cases for Problem 4
def test_add_n_items():
    print("\n--- Testing add_n_items(6) ---")
    add_n_items(6)
    print("\n--- Testing add_n_items(10) ---")
    add_n_items(10)
    print("✅ Manual verification needed - check resize patterns above!")

test_add_n_items()


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
- Trade-offs: Uses O(n) space for output. Could modify input list in-place for O(1) extra space,
  but that would destroy original data. Current approach preserves input immutability.
"""

# Test cases for Problem 5
def test_running_total():
    # Basic case
    assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
    # Single element
    assert running_total([5]) == [5]
    # Empty list
    assert running_total([]) == []
    # With zeros
    assert running_total([1, 0, 2, 0, 3]) == [1, 1, 3, 3, 6]
    # Negative numbers
    assert running_total([1, -1, 2, -2]) == [1, 0, 2, 0]
    # All negative
    assert running_total([-1, -2, -3]) == [-1, -3, -6]
    # Large numbers
    assert running_total([100, 200, 300]) == [100, 300, 600]
    print("✅ All tests passed for running_total!")

test_running_total()


print("\n" + "="*50)
print("🎉 ALL TESTS COMPLETED!")
print("="*50)
