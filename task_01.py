#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Producing Half-Cartesian"""


def get_matches(players):
    """This function produces a list of unique conbination for given dataset.

    Args:
        players(mixed): list of string or int.

    Returns:
        A list of tuples containing unique matchups between given dataset.

    Examples:
        >>> get_matches(['James', 'Jesse', 'Jennifer'])
        [('James', 'Jesse'), ('James', 'Jennifer'), ('Jesse', 'Jennifer')]
        >>> get_matches(['you', 'me', 'she'])
        [('you', 'me'), ('you', 'she'), ('me', 'she')]
        >>> get_matches([1, 2, 3])
        [(1, 2), (1, 3), (2, 3)]

    """
    matches = []
    for index1, p_1 in enumerate(players):
        if index1 < (len(players)-1):
            for index2, p_2 in enumerate(players):
                if index1 < index2:
                    matches.append((p_1, p_2))
    return matches
