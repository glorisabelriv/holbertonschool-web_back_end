#!/usr/bin/env python3
""" Implement a method named get_page that takes two integer
    arguments page with default value 1 and page_size
    with default value 10.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """ Index_range
        Argumentos:
            `page`: current page number
            `page_size`: items number in every page
        Return:
            list for those particular pagination parameters
    """
    start: int
    end: int

    if page == 1:
        start = 0
    else:
        start = (page - 1) * page_size

    end = page * page_size

    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ paginate the dataset correctly and
            return the appropriate page of the dataset
        """

        assert (type(page) == int)
        assert (type(page_size) == int)
        assert (page > 0)
        assert (page_size > 0)
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        return dataset[start: end]
