def get_indices_of_item_weights(weights, length, limit):
    """
    This function instantiates a hash table, then puts indices of
    item weight in the hash table with the key being their weight.

    After each deposit, it checks (O(1)) the keys in order to see if
    a complement is present. If it's present, it queries the hash
    table to pull the second index (the current item being hashed
    will contain the first index.

    Some code is clunky -- the edge case of "items that are exactly
    half of the weight of the backpack" is a bit awkward. This code
    could likely be refactored in order to move where it "checks"
    for whether the remaining space in the backpack is equal to
    an extant key before it writes anything in the hash table.

    The code, though clunky, I believe is O(n): all the lookups and
    hash table writes are O(1), so worst-case scenario we have O(1)
    multiplied by having to go through n items.
    """
    hash_table = {}

    for i in range(length):
        if weights[i] in hash_table.keys():
            hash_table[weights[i]] = [hash_table[weights[i]], i]
        else:
            hash_table[weights[i]] = i

        remaining_weight = limit - weights[i]
        if remaining_weight == weights[i]:
            if isinstance(hash_table[remaining_weight], list):
                indices = sorted(hash_table[remaining_weight], reverse=True)
                return indices
            else:
                continue

        if remaining_weight in hash_table.keys():
            weights = [remaining_weight, weights[i]]
            indices = sorted([hash_table[weight] for weight in weights], reverse=True)
            return indices

    return None

weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
