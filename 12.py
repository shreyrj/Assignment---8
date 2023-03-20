tuples_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_tuples_list = sorted(tuples_list, key=lambda x: x[1])

print("Sorting the List of Tuples:", sorted_tuples_list)
