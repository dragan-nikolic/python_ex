# question: I’m going to give you a piece of code. Tell me what’s wrong with it.

def add_items(val, list=[]):
    list.append(val)
    return list

print(add_items(1))  # Output: [1]
print(add_items(2))  # Output: [1, 2]

# fixed version
def add_items2(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list

print(add_items2(1))  # Output: [1]
print(add_items2(2))  # Output: [2]
