# Aysmptotic Notation

# 1. Big O
# 2. Big Omega
# 3. Big Theta

# 1. Big O - upper bond (worst case)
lst = [6,4,1,5,89,12,3,45,67,12,3]
# Worst Case = lst[10] / lst[-1]   # 11 iterations

# f(n) <= c.g(n)
# n^0 <= n
# n^0 >= 1
# f(n) = O(g(n))


# 2. Big Omega - lower bond (best case)
lst = [6,4,1,5,89,12,3,45,67,12,3]
# Best Case = lst[0]               # 1 iteration

# f(n) >= c.g(n)
# n^0 <= n
# n^0 >= 1
# f(n) = Ω(g(n))



# 3. Big Theta - (average case )
lst = [6,4,1,5,89,12,3,45,67,12,3]
# Average Case = lst[5]            # 6 iterations


# c1.g(n) <= f(n) <= c2.g(n)
# n^0 <= n
# n^0 >= 1
# f(n) = Θ(g(n))

# n     -> input
# t     -> time 
# f(n)  -> code/function/method
# c     -> constant
# g(n)  -> time complexity
# n^0   -> the threshold after it the input cannot beyond the upper bond and below lower bond