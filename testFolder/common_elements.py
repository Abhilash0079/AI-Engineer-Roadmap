def find_common_elements(list_a: list[int], list_b: list[int]) -> list[int]:
    common_element = []

    for element in list_a:
        if element in list_b and element not in common_element:
            if element in common_element:
                continue
            else:
                common_element.append(element)

    return common_element

list_a = [1, 2, 3, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
result = find_common_elements(list_a, list_b)
print(f"Common Elements: {result}")

print(find_common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print(find_common_elements([1, 3, 3, 4], [3, 4]))