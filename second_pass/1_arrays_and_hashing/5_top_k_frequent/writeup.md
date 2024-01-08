# Top K Frequent Elements

This problem is a bit tricky but it has a solution that works by reversing the counts to the hashmap. An important concept to look into before this is [Bucket Sort](https://www.geeksforgeeks.org/bucket-sort-2/)

## Solution 1: Bucket-Sort Style Hashmap
The idea of this solution is similar to how bucket sort works. We need to put each element in the `nums` array into a bucket that corresponds to its frequency, or count. The first step to this solution is to create a hashmap of frequencies, which can easily be done in a single iteration. 

Now that we have the `map`, we need a way to reverse the map. Essentially, what we want is a way where the key of the `map` is the frequency of the number, and the `value` of the map is any or all the numbers that have that map. 

This can be done using a hashmap, but a better data structure to use here is an array. This is because, not only we need to know which numbers belongs to which count, we also need to know the biggest count, and the second biggest count, and so on. 

The solution to this is an array called `counts` of size `n + 1` where `counts[i] = k` means there are `i` number of elements of `k` in the original array `nums`. This is the reason for making the `counts` of size `n + 1` so that `n` is a possible index. This is to accommodate the case where the entire `nums` is a single number, hence the count of that number is `n`

But in the `nums`, there can be multiple numbers having the same count. This can be easily fixed by making `counts` an array of array. So in this way, `counts[i] = []` reads as "All the numbers in `nums` that have the count of `i`"

Once we are able to build this array, we simply need to traverse in a descending order and pick the numbers until we have picked `k` numbers. 

### Code
```
# Build the hashmap for counting
map = {}
for num in nums:
    if num in map:
        map[num] += 1
    else:
        map[num] = 1

# Initialize the counts array
counts = []
n = len(nums)
for i in range(n + 1):
    counts.append([])

# Populate the counts array
for key, value in map.items():
    counts[value].append(key)

# Pick the last k elements
final = []
added = 0
for i in range(n, 0, -1):
    for num in counts[i]:
        final.append(num)
        added += 1
        if added == k:
            break

    if added == k:
        break

return final
```

### Complexity Analysis
The time complexity of the above solution is a bit tricky to find, but let's break it down into smaller sections.

The first loop is simply a counter so that is `O(N)` 

The second loop is used for initialization of the `counts` array, and it's `O(N + 1)`

The third loop goes over the unique elements and their counts. At worst, each element in the `nums` array can present once, forcing us to basically iterate over `nums` itself. This means, at worst it is `O(N)` 

Now we have two loops. The outermost loop is going in descending order so it can assumed to be `O(N)` but it actually breaks when it hits `K` number of elements. So in actuality the loop is going `O(K)` as well. The condition in the innermost loop is also the same as the outermost loop, even though it is iterating over `counts[i]` it will break once it reaches `K` elements. So both loops have a combined complexity of `O(K)`

This adds up to `O(N + N + 1 + N + K) => O(3N + K + 1) => O(N + K)`

The space complexity of the solution can be found by basically adding up all the variables used for storage, and assuming that all of them have to store `N` numbers at worst. So `O(N + N + N + 1) => O(3N + 1) => O(N)`

