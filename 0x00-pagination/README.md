# 0x00. Pagination (Back-end)

This project focuses on implementing pagination for a back-end application. Pagination is a crucial feature when dealing with large datasets. It allows you to divide and present data in manageable chunks, improving the user experience and application performance. In this project, you will learn how to implement different pagination techniques and handle scenarios where data may change or be deleted.

## Learning Objectives

- Understand how to paginate a dataset with simple `page` and `page_size` parameters.
- Implement pagination with hypermedia metadata.
- Develop a deletion-resilient pagination mechanism.

## Tasks

### Task 0: Simple Helper Function

In this task, you will create a simple helper function named `index_range` that takes two integer arguments, `page` and `page_size`. The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters. Page numbers are 1-indexed, meaning the first page is page 1.

### Task 1: Simple Pagination

For this task, you will implement a class called `Server` that deals with paginating a database of popular baby names. The `Server` class should have a method called `get_page` that takes two integer arguments, `page` and `page_size`, with default values of 1 and 10, respectively. You should use the provided CSV file, and the `assert` statement to ensure valid input. The `get_page` method should return the appropriate page of the dataset, and if the input arguments are out of range, it should return an empty list.

### Task 2: Hypermedia Pagination

This task builds upon the previous one. You need to implement a `get_hyper` method in the `Server` class that takes the same arguments and defaults as `get_page`. It returns a dictionary containing key-value pairs with hypermedia metadata, including the current page's size, page number, data, next page, previous page, and the total number of pages. You should reuse the `get_page` method in your implementation.

### Task 3: Deletion-Resilient Hypermedia Pagination

In this task, you'll implement a `get_hyper_index` method within the `Server` class. This method takes two integer arguments, `index` and `page_size`, with default values. It returns a dictionary with hypermedia metadata, similar to the `get_hyper` method. However, the focus here is to ensure that if rows are removed from the dataset between two queries, the user does not miss items when changing pages. The method should handle scenarios where data is deleted, and the pagination remains consistent.

---

## How to Use

1. Clone this repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd 0x00-pagination`
3. Implement the required functions and methods in the respective Python files.
4. Use the provided test scripts to validate your implementation.
   - For Task 0: `./0-main.py`
   - For Task 1: `./1-main.py`
   - For Task 2: `./2-main.py`
   - For Task 3: `./3-main.py`

---

## Repository Information

- GitHub Repository: [alx-backend](<repository-link>)
- Directory: 0x00-pagination

Please refer to the individual Python files in the repository for the code related to each task.

---

This project will help you understand the essential concepts of pagination in a back-end context and develop robust pagination mechanisms. Have fun coding! 😊
