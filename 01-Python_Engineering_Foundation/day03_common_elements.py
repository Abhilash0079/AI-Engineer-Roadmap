list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

common_elements = []

for ele in list_a:
    if ele in list_b:
        common_elements.append(ele)
        
print(common_elements)