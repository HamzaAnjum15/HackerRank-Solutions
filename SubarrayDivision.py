# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

# Lily decides to share a contiguous segment of the bar selected such that:

# The length of the segment matches Ron's birth month, and,
# The sum of the integers on the squares is equal to his birth day.
# Determine how many ways she can divide the chocolate.

# s = [2,2,1,3,2]
# d = 4
# m = 2 
# ily wants to find segments summing to Ron's birth day,  with a length equalling his birth month, . In this case, there are two segments meeting her criteria:  and .
def birthday(s, d, m):
    # Write your code here
    count = 0
    total = sum(s[:m])
    if total == d:
      count += 1
    
    for i in range(m, len(s)):
      total += s[i]  # Add the next element in the sequence
      total -= s[i-m]  # Subtract the element that moves out of the window
      if total == d:
        count += 1
    return count
