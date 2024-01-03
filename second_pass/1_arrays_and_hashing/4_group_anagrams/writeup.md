# Group Anagrams

This problem seems like its tricky at first but it actually has a counter-intuitive solution.

## First Solution - Brute Force
Recall that we have already solved the problem of determining if two strings are valid anagrams or not. This is solved in the `2_valid_anagram` problem. The most optimal solution to that problem requires time complexity of `O(n)` and a space complexity of `O(1)`

This means that a brute force solution to this problem needs to go over every pair in the `strs` list, and check to see if they are anagram pairs. This can be written in code like this
```
n = len(strs)
for i in range(n):
    first_string = strs[i]
    for j in range(i + 1, n):
        second_string = strs[j]
        if valid_anagram(first_string, second_string):
            # Code for adding this in the group
```

### Complexity Analysis
The outer loop executes `n` time since it needs to iterate over all the strings in the array. The second loop however, iterates like `n - 1, n - 2, n - 3, ...., 3, 2, 1, 0` therefore the sum of this arithmetic series is given by: `S = n(n - 1) / 2` 

The time complexity of the function `valid_anagram` is `O(n)` so the combined time complexity of this solution is `O(n(n - 1)n) => O(n ^ 3)`

## Second Solution - Hash and Sort

Obviously `O(n ^ 3)` is not the ideal solution, and we need to find a way to use a hashmap here. The problem with using a hashmap is that it needs a way to compare two anagram strings as one, so that they are "bucketed" in a single array inside hashmap. 

Consider this: We have a a hashmap `map` where `map[str] = []` meaning `str` is an unique string identifier that identifies this group of anagrams. All strings inside `map[str] = []` are going to be anagrams of `str`

So this means we need a way to compare two strings as anagrams of each other, that can work in the hashing function. Our current approach of determining valid anagrams is `O(n)`. Another way of checking anagram is **sorting** the strings and simply comparing them

Since sort takes `O(nlogn)` at worst, this method of comparing anagrams is going to be worst than our optimal method, but it will help in the overall grouping of the anagrams

The code for this solution looks like this:
```
map = defaultdict(list)
n = len(strs)
for i in range(n):
    new = ''.join(sorted(strs[i]))
    map[new].append(strs[i])

return list(map.values())
```

The line 
```
new = ''.join(sorted(strs[i]))
```

sorts the string `strs[i]`. Two sorted strings are equal to each other if they are anagrams of each other. So this property allow us to use the hashmap


### Complexity Analysis
In a bit of a counter-intuitive way, this approach is the optimal solution to this problem. The main loop only runs for `n` iterations. Meanwhile, the sorting takes `O(nlogn)` time complexity. This means this solution can reduce the time complexity from `O(n ^ 3)` to `O(n ^ 2 log n) => O(n ^ 2)` which is a degree better than the previous one

The space complexity of this solution will be `O(1)` since the hashmap is part of the result