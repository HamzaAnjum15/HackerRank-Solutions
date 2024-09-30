#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
# Sample Input 1 2 3 4 5
# Sample Output 10 14

def miniMaxSum(arr):
    # Sort the array
    arr.sort()
    
    # Sum of the first 4 elements for the minimum
    mini = sum(arr[:4])
    
    # Sum of the last 4 elements for the maximum
    maxx = sum(arr[1:])
    
    # Print the result as required
    print(mini, maxx)
