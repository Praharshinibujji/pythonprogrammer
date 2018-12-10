def maximum_num_in_list( list ):
    maximum = list[ 0 ]
    for a in list:
        if a > maximum:
            maximum = a
    return maximum
print(maximum_num_in_list([5,4,3,2,1,7,6,10,8,9]))

