# empty list
stack = []

# Push a new item in the list. First in last out. The C will be on the top.
# Order from top to bottom is CBA
stack.append("A")
stack.append("B")
stack.append("C")
print("stack: ", stack)

# pop the top item in the list which is c
element = stack.pop()
print("pop", element)

# peek: means check the top item on the list.
top_element = stack[-1]
print("top", top_element)

# see if the stacks is empty
is_empty = not bool(stack)
print("is_empty", is_empty)

# size of the stacks, lengths 
print("size: ", len(stack))
