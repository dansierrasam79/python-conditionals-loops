# compute sum and average of n numbers
import statistics
num_limit = int(input("Enter a number: "))
lst = [num for num in range(num_limit+1)]
print("Total: ", sum(lst))
print("Average: ", statistics.mean(lst))
