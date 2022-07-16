from typing import Iterable


def flatten_gen(items):
    """Yield items from any nested iterable; see Reference."""
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten_gen(x):
                yield sub_x
        else:
            yield x


def flatten(nested):
    """Flatten any nested iterable; see Reference."""
    out = []
    for inner in nested:
        for item in inner:
            out.append(item)
    return out
    # flatitems = [num for num in flatten(nested)]
    # flat_list = [num for sublist in nested for num in sublist]
    # print(flat_list)


def unroll(items):
    if type(items) != list:
        # not a list - could be an iterator though
        return items
    elif type(items) == list and type(items[0]) != list:
        # not nested
        return items
    # if (type(items[0]) is not list):
    #     return items
    flat = flatten(items)
    # flat = [item for item in generator]
    print('input:', items, ' flat=>', flat, type(flat))
    return flat

# print(flatten(nested))


def test():

    nest4 = [
        ['item1', 'item2', 'item3']
    ]

    nest1 = [[1], [2, 3]]

    nest2 = {
        'a': 1, 'b': 2
    }
    # print(flatten(nest2))

    nest3 = [1, 2, 3, 4]

    # print(unroll(nest1))
    # print(unroll(nest2))
    # print(unroll(nest3))
    result = unroll(nest4)
    print('result', result)


test()
