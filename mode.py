#Returns the most frequent number on a list of numbers.
def mode(lista):
    data = {key:lista.count(key) for key in lista}
    # find the highest value (the most frequent number)
    max_value = max(data.values())
    # now we need to see at which index the highest value is at
    correct_index = list(data.values()).index(max_value)
    # finally, return the correct key for the correct index (we have to convert cou)
    return list(data.keys())[correct_index]

#mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4