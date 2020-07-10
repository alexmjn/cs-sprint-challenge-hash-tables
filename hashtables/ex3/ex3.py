from collections import Counter

def intersection(arrays):
    """
    First: we need to unpack these arrays. We can do this with a list
    comprehension. Secondly: we need to create a hash table from the arrays.
    Counter() is useful here; we can simply count the incidence of each element
    in the arrays and then return all keys to where the count of such keys
    is equal to the number of arrays.

    Note this currently runs the test at around 8 seconds.
    """
    our_table = Counter()
    for i in range(len(arrays)):
        for j in arrays[i]:
            our_table[j] += 1

    list_results = [key for key in our_table.keys()
     if our_table[key] == len(arrays)]

    return list_results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
