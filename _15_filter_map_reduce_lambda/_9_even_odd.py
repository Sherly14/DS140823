lst = [12,56,75,3,12,78]
even_odd = list(map(lambda lst : "Even" if lst%2 == 0 else "Odd",lst))
print(even_odd)