# count even and odd nums
nums = [i for i in range(0,10)]
evens = [num for num in nums if num % 2 == 0 ]
odds = [num for num in nums if num % 2 != 0 ]
print(len(evens))
print(len(odds))