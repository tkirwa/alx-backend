def index_range(page, page_size):
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
    end_index = start_index + page_size

    return (start_index, end_index)


# This allows the script to be run independently for testing
if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
