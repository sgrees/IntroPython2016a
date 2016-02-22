feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
comprehension = [delicacy.capitalize() for delicacy in feast]
print(comprehension[0])
print(comprehension[2])

comp = [delicacy for delicacy in feast if len(delicacy) > 6]
print(len(feast))
print(len(comp))
