import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of the start and end indexes for a given page and page
      size.

    Args:
    - page (int): The page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - tuple: A tuple containing the start and end indexes.
    """
    if page < 1 or page_size < 1:
        return (0, 0)  # Invalid input, return an empty range

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
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
