from singleton_object import SingletonObject

# Instantiate the first object.
first = SingletonObject()
# Set the value.
first.val = 'Object value 1'
print('obj1.val: ', first)

print('------')
# Instantiate the second object.
second = SingletonObject()
# Set the value.
second.val = 'Object value 2'

# The values are the same in both objects.
assert first.val is second.val
print('obj1.val: ', first)
print('obj2.val: ', second)
