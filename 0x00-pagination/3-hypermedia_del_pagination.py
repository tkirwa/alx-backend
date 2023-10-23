#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get a hypermedia page by specifying the start index (index) and page
          size (page_size).
        Args:
            index (int): The start index for the page.
            page_size (int): The size of the page.
        Returns:
            dict: A dictionary containing page information.
        """
        assert (index is None or isinstance(index, int)) and isinstance(
            page_size, int) and page_size > 0, "Invalid input parameters"

        indexed_dataset = self.indexed_dataset()

        if index is None:
            # If index is None, start from the beginning.
            index = 0

        data = []
        next_index = index

        for i in range(index, index + page_size):
            if i in indexed_dataset:
                data.append(indexed_dataset[i])
                next_index = i + 1

        return {
            "index": index,
            "page_size": page_size,
            "data": data,
            "next_index": next_index if next_index < len(
                indexed_dataset) else None
        }
