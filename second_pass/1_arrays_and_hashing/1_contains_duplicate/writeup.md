# Contains Duplicate

A fairly simple question to solve. Since we don't actually need to find the duplicates, and we just need to tell if duplicates exist or not

## Simplest Solution
Of course the most simple solution would be to use double `for` loops.
Pick an element, check if that element exists in the array.
Sample pseudo code for this:

```
for i in range(len(nums)):
    current = nums[i]
    for b in range(i + 1, len(nums)):
        if current == nums[b]:
            return True

return False
```

Mathematically this is `O(n^2)` since the first loop runs over `n` times and the other loop runs for `SUM(n - 1, n - 2, n - 3, n - 4 ... 0) = n` times

## Improve using Hashmap

The `O(n^2)` can be converted into an `O(n)` by using a hashmap. The idea is to first add everything inside a hashmap, and then use the hashmap to check if the element is already added or not

This can be simply done through:
```
hashmap = {}
for num in nums:
    if num in hashmap:
        return True
    hashmap[num] = 1 # doesn't matter what value we assign to it
return False
```

## Simpler Solution

An even simpler solution to this is to use Python's built-in `set` data structure, and convert the initial `list` to `set`. We can then just simply compare the length of the two entities and any difference will result in a duplicates being found

```
return len(list(set(num))) != len(nums)
```
