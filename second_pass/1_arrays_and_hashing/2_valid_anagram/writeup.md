# Valid Anagram

Another problem that can be solved using the hashmap. This problem teaches you to look at the constraints more closely

## Simple Solution
Check to make sure that the lengths of the strings are the same. This is a low hanging fruit

The first solution that comes to my mind is to of course to count all the letters in the first string `s`, then use that counts to subtract the counts from the `t` string, and finally check if the hashmap has counts of zero.

This can be coded like this:
```
if len(s) != len(t):
    return False

map = {}
for letter in s:
    if letter in map:
        map[letter] += 1
    else:
        map[letter] = 1

for letter in t:
    if letter in map:
        map[letter] -= 1
        if map[letter] < 0: # a check to see if the count has already gone below zero
            return False
    else:
        return False # a letter in t that is not in s isn't valid anagram

for value in map.values():
    if value != 0:
        return False
```

This way of counting and subtracting means that we need to account for cases where a letter may be more in `s` than in `t` or vice versa. Therefore we need proper checks

### Analysis
If the length of the string `len(s) = len(t) = n` than this method is of `O(3n) => O(n)` time complexity, and it uses a space of `O(n)` 

## Cleaner Solution
We can make further optimization to this solution and turn it into a `O(1)` space complexity, and do it in two for loop as well. The idea here is to understand the constraints. The constraints says that `s` and `t` are going to be lowercase english letters only. This is an important mathematical thing to note, since this means there will only be `26` characters in total. 

So how can we use this information? Well instead of counting the occurrences of the letters in the two strings, we count how many times these alphabets appear. This reduces the complexity of knowing which character is in the two string or not

Here, we can also remove the hashmap. All the english letters can be mapped to numbers like `a => 0, b => 1, ... z => 25` so that means we can use an array of length `26`. Lets call this array `count`. So `count[i]` is the count of the ith alphabet. 

Since characters are in ASCII, we need to subtract out the ASCII character offset. This can be done using the `ord` function, so `offset = ord("a")`

We combine all this to give us the following solution
```
if len(s) != len(t):
    return False

alphabets = [0] * 26

offset = ord("a")

for i in range(len(s)):
    alphabets[ord(s[i]) - offset] += 1
    alphabets[ord(t[i]) - offset] -= 1

for j in range(26):
    if alphabets[j] != 0:
        return False

return True
```

Few things to note here:
1. We iterate over `n` which is the length of both of the strings
2. In each iteration, we add to the count of the letter in `s` and decrease the count of the letter in `t`
3. In this way, if both strings are anagrams, the count will cancel each other out
4. Finally, we make use of the `alphabets` array and make sure that all the counts of it are `0`

### Analysis
This solution improves on the first by reducing the space required. We use `O(26) => O(1)` space here, and the time complexity also goes down by `O(n + 26) => O(n)` 