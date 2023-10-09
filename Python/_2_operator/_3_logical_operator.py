# Logical Operator

# and - if all the conditions are true than only it will return True else False
# or  - if atleast one condition is true than only it will return True else False
# not - it will return True for False condition and vice versa

no1 = 10
no2 = 20

and_demo = no1 == no2 and no2 > 5
print("And : ",and_demo)

or_demo = no1 == no2 or no2 < 5
print("Or : ",or_demo)

not_demo = not(no1 != no2)
print("Not : ",not_demo)
