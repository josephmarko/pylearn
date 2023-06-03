def sum_of_squares_and_product(list1, list2): 
        sum_of_squares = sum([x**2 for x in list1]) 
        product = 1
        for x in list2:
                product *= x
        return sum_of_squares, product

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = sum_of_squares_and_product(list1, list2)

print(result)