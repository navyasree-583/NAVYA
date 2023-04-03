def square(n):
    return n*n
my_list = [2,3,4,5,6,7,8,9]
updated_list = map(square, my_list)
print(updated_list)
print(list(updated_list))

my_tup=(1,2,3,5,6,7,9)
updated_tup=map(square,my_tup)
print(updated_tup)
print(tuple(updated_tup))

my_set={1,2,3,5,6,7,9}
updated_set=map(square,my_set)
print(updated_set)
print(set(updated_set))

my_dict={'a':1,'b':2}
updated_tup=map(square,my_dict.values())
print(updated_tup)
print(list(updated_tup))
