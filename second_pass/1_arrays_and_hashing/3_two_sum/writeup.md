# Two Sum
Another problem that can be solved similar to how we solved contains duplicate. 

## First Solution - Two Pass Hashmaps
The idea here is that, two numbers add to `target`. If we are iterating over the array `nums`, This happens:

1. We will get a number `num` at index `i`
2. The objective here is to find another number `x` that satisfies `num + x = target`. This means `x = target - num`. Since now we know that value of `x` the problem boils down to finding this number in the array
3. For this, we use a hashmap. We store all the numbers of the array in the hashmap first, and then use it to find the number.
4. This problem is helped by the constraint that only one solution exist in the array

The code for this looks like this:
```
map = {}
for i, num in enumerate(nums):
    map[num] = [i]

for i, num in enumerate(nums):
    to_find = target - num
    if to_find in map:
        index = map[to_find]
        return [index, i]

return None
```

### Dealing with duplicates
Notice how we don't have any special code for dealing with duplicates. In the hashmap, we only need to store the index of only one of the element of the array if duplicates of that element exist. 

For example, given `nums = [1, 2, 3, 4, 3, 4, 3]`, `map[3] = 6` because the hashmap will store the index of the last element of the array.

Now why is this not a problem? Since the second loop iterates from left to right, we will first try to match the `3` in the third position with the `3` in the 6th position. This automatically takes care of the duplicate problem.

Consider another case: `nums = [3, 3], target = 6` 

In this case, `map[3] = 1` since that was the last `3` in the `nums` array. Since the target is 6, the first `3` needs to match with the second `3` to be considered a valid solution. 

### Complexity Analysis
The time complexity of the above solution is `O(2n) => O(n)` since we traverse the list twice. 

The space complexity of the solution is `O(n)` at worst since we need to store `n` items in the hashmap

## Second Solution - One Pass Hashmap

This solution can be improved by using only a single loop instead of using two different loops. In this case, we have to build and use the hashmap in the same iteration. 

Since we traverse the array from left to right, the hashmap will also be built from left to right, so at each point in the iteration, all elements before `i` are added in the hashmap and can be used in the calculation. This approach can be written simply like

1. Get `x = target - num` 
2. Find `x` in the hashmap
3. If found, return the solution, otherwise add `num` in the hashmap

Notice how we check we do the checking of the hashmap first, and build it later. This is to handle the case where there are duplicates, and we need both numbers to reach the target.

For example: `nums = [3, 3], target = 6` 

In the above case, if we add the second `3` in the hashmap first, it will overwrite the first `3` in the hashmap, and we won't be able to find the first `3` as its complement. 

The code for this is given below
```
hashmap = {}
for i in range(len(nums)):
    complement = target - nums[i]
    if complement in hashmap:
        return [i, hashmap[complement]]
    hashmap[nums[i]] = i
```

### Complexity Analysis
The time complexity of this solution will be the same `O(n)` and the space complexity will be `O(n)`