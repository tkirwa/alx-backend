#!/usr/bin/env python3
"""1. Simple pagination"""

import csv
from typing import List, Tuple
from math import ceil


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end index for pagination.
    Args:
        page (int): The current page.
        page_size (int): The number of items per page.
    Returns:
        Tuple[int, int]: A tuple containing the start and end indexes.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


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
        """
        Retrieves a page of data from the dataset.
        Args:
            page (int): The page number (default is 1).
            page_size (int): The number of items per page (default is 10).
        Returns:
            List[List]: A list of rows representing the dataset page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        total_rows = len(dataset)
        start, end = index_range(page, page_size)

        if start >= total_rows:
            return []  # Page is out of range, return an empty list.

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retrieves a page of data and hypermedia-style pagination information.
        Args:
            page (int): The page number (default is 1).
            page_size (int): The number of items per page (default is 10).
        Returns:
            dict: A dictionary containing pagination information.
        """
        page_data = self.get_page(page, page_size)
        total_rows = len(self.dataset())
        total_pages = ceil(total_rows / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        pagination_info = {
            "page_size": page_size,
            "page": page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return pagination_info
