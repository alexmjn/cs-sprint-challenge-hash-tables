from collections import Counter
def has_negatives(a):
    """
    Again, using the Counter() object, then accessing its keys directly,
    then transforming it through a list comprehension.
    """
    our_dict = Counter()
    for integer in a:
        our_dict[integer] += 1

    result = [integer for integer in our_dict.keys()
    if integer > 0 and our_dict[-integer] > 0]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
