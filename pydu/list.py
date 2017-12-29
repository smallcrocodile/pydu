from collections import OrderedDict
def uniq(seq, key=None):
    """
    Removes duplicate elements from a list while preserving the order of the rest.

    The value of the optional `key` parameter should be a function that
    takes a single argument and returns a key to test the uniqueness.
    """
    # return iterator -> OrderedDict.fromkeys(seq).keys()
    return list(OrderedDict.fromkeys(seq))
        
