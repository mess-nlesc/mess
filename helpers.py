"""Set of functions to manupulate the data"""

from itertools import product


def combine_variables(input_dictionary):
    """Returns a product (combinations) of vectors
    """
    for dict_product in product(*input_dictionary.values()):
        yield dict(zip(input_dictionary.keys(), dict_product))
