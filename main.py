## Lists are mutable objects
## Mutable - can have their value changed after they are created

my_list = [1, 2, 3]
print(my_list)

## changing list value
my_list[1] = 7
print(my_list)


## Tuples are Immutable objects
## Immutable - value cannot be changed after they are created
my_tuple = (1, 2, 3)
print(my_tuple)

## id() - tells the identity of an object in Python
## print(id(my_tuple))
## print(id(my_list))

## strings are also Immutable
my_string = "hello"
print(my_string)

