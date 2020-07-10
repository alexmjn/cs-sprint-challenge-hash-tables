# Your code here



def finder(files, queries):
    """
    Strategy: create a hash table of possible queries (the ends of file
    names), where each key is the file name and each value is the
    possible paths attached to that file name.

    First, we break up the files and pop out the file names. Next, for each
    of those file names, we attach the rest of the full path as a value
    in the dictionary.

    Finally, we run through our queries -- if they're in the dictionary,
    we reattach the full path to the filename and return it as part of
    our results; if they aren't, we continue the loop.
    """
    path_dict = {}

    for path in files:
        split_strings = path.split("/")
        file_name = split_strings.pop()
        rest_of_path = "/".join(split_strings)

        if file_name in path_dict.keys():
            path_dict[file_name].append(rest_of_path)

        else:
            path_dict[file_name] = [rest_of_path]

    result = []

    for query in queries:
        # combine filename, if it exists, with all existing paths to that file
        if query in path_dict.keys():
            for path in path_dict[query]:
                found_file = (path + "/" + query)
                result.append(found_file)
        else:
            continue

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
