
# Find Largest Element

def get_largest_element(lst):

    max_value = lst[0]

    for item in lst:
        if item > max_value:
            max_value = item

    return max_value 

lst = [3,8,9,12,45,1,2]

print(get_largest_element(lst))
