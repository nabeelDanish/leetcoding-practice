# Product of Array Except Self

A bit of a tricky problem that requires clean code implementation

## Solution 1 - Brute Force

Before we even start the brute force solution, what will the solution look like if we are allowed to use the division operator. The code for that is:
```
product = 1

for num in nums:
    product *= num

for i in range(len(nums)):
    nums[i] = nums[i] / product

return nums
```

Since we are not allowed to use the division operator, the brute force way is to compute the product for each number individually. Essentially running two loops to compute the product. This can be done like this

```
result = []
n = len(nums)
for i in range(n):
    result.append(0)
    
    product = 1
    for j in range(n):
        if j != i:
            product *= nums[j]
    
    result[i] = product

return result
```

This solution runs in `O(N ^ 2)` time, and of course, fails the time limit criteria. The goal of the problem is to do this in `O(N)` time. 

## Solution 2 - Prefix and Suffix Arrays
Let's try to understand what the solved array will look like. Given the solved array `product`, `product[i]` is the product of all the elements in the array `nums` without `nums[i]` 

This statement can also be thought as this: `product[i]` is the product of all the elements to the left of `nums[i]` and all the elements to the right of `nums[i]` 

Which means: `product[i] = left_except_i[i] * right_except_i[i]`

Lets call `left_except_i` as `prefix` and `right_except_i` as `suffix`

So, `prefix[i]` is the product of all the elements to the left of `i` except `i` in `nums`. And `suffix[i]` is the product of all the elements to the right of `i` except `i` in `nums`

So how do we build these arrays? Well whatever the value of `prefix[i]` is, it can be reused in `prefix[i + 1]` after multiply it with `nums[i]`. So `prefix[i] = prefix[i - 1] * nums[i - 1]`

And in the same way, `suffix[i] = suffix[i + 1] * nums[i + 1]`

So the new solution to this problem looks like this:
```
n = len(nums)
prefix = [1] * n
suffix = [1] * n

for i in range(1, n):
    prefix[i] = nums[i - 1] * prefix[i - 1]

for i in range(n - 2, -1, -1):
    suffix[i] = suffix[i + 1] * nums[i + 1]

product = [1] * n
for i in range(n):
    product[i] = prefix[i] * suffix[i]

return product
```

## Solution 3 - Without Using Additional Arrays
If we observe the prefix and the suffix array, we realize that they are a bit redundant. For example, in the case of `nums = [1, 2, 3, 4]`, the prefix array builds up to be `prefix = [1, 1, 2, 6]` and `suffix = [24, 12, 4, 1]`

We can see that the product from both the left-hand side and the right-hand side increases, and we only use the last product. So we need to find a way to combine this without using the additional arrays

If we initialize the product array to be `product = [1] * n` than we need a way to multiply it with `prefix` and `suffix` without using the arrays. This will require two passes over the `nums` and `product` array, since the first pass goes from left to right, and the second pass goes from right to left

This can be done like this
```
n = len(nums)
product = [1] * n

left = nums[0]
for i in range(1, n):
    product[i] = left
    left = left * nums[i]

right = 1
for i in range(n - 1, -1, -1):
    product[i] = product[i] * right
    right = right * nums[i]

return product
```
