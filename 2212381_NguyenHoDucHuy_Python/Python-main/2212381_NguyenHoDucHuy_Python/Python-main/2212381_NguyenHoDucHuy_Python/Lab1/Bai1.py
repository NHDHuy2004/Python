
def is_value_in_group(value, group):
    return value in group


test_value1 = 3
test_group1 = [1, 5, 8, 3]
test_value2 = -1
test_group2 = [1, 5, 8, 3]


print(f"{test_value1} -> {test_group1} : {is_value_in_group(test_value1, test_group1)}")
print(f"{test_value2} -> {test_group2} : {is_value_in_group(test_value2, test_group2)}")
