# 0x01. Caching (Back-end)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system is
- What limits a caching system has

## Requirements

### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python3 (version 3.7).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the pycodestyle style (version 2.5).
- All your files must be executable.
- The length of your files will be tested using `wc`.
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)`).
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)`).
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)`).
- A documentation is not a simple word; it's a real sentence explaining what's the purpose of the module, class, or method (the length of it will be verified).

## Tasks

### 0. Basic dictionary

Create a class `BasicCache` that inherits from `BaseCaching` and is a caching system:
- You must use `self.cache_data` - a dictionary from the parent class `BaseCaching`.
- This caching system doesn't have a limit.
- `def put(self, key, item)`:
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
- `def get(self, key)`:
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn't exist in `self.cache_data`, return `None.

### 1. FIFO caching

Create a class `FIFOCache` that inherits from `BaseCaching` and is a caching system:
- You must use `self.cache_data` - a dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):` but don't forget to call the parent init: `super().__init__()`.
- `def put(self, key, item)`:
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
        - You must discard the first item put in cache (FIFO algorithm).
        - You must print `DISCARD:` with the `key` discarded and followed by a new line.
- `def get(self, key)`:
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn't exist in `self.cache_data`, return `None.

### 2. LIFO Caching

Create a class `LIFOCache` that inherits from `BaseCaching` and is a caching system:
- You must use `self.cache_data` - a dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):` but don't forget to call the parent init: `super().__init()`.
- `def put(self, key, item)`:
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
        - You must discard the last item put in cache (LIFO algorithm).
        - You must print `DISCARD:` with the `key` discarded and followed by a new line.
- `def get(self, key)`:
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn't exist in `self.cache_data`, return `None.

### 3. LRU Caching

Create a class `LRUCache` that inherits from `BaseCaching` and is a caching system:
- You must use `self.cache_data` - a dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):` but don't forget to call the parent init: `super().__init()`.
- `def put(self, key, item)`:
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
        - You must discard the least recently used item (LRU algorithm).
        - You must print `DISCARD:` with the `key` discarded and followed by a new line.
- `def get(self, key)`:
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn't exist in `self.cache_data`, return `None.

### 4. MRU Caching

Create a class `MRUCache` that inherits from `BaseCaching` and is a caching system:
- You must use `self.cache_data` - a dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):` but don't forget to call the parent init: `super().__init()`.
- `def put(self, key, item)`:
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
        - You must discard the most recently used item (MRU algorithm).
        - You must print `DISCARD:` with the `key` discarded and followed by a new line.
- `def get(self, key)`:
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn't exist in `self

.cache_data`, return `None.

### 5. LFU Caching (Advanced)

Create a class `LFUCache` that inherits from `BaseCaching` and is a caching system:
- You must use `self.cache_data` - a dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):` but don't forget to call the parent init: `super().__init()`.
- `def put(self, key, item)`:
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
        - You must discard the least frequently used item (LFU algorithm).
        - If you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used.
        - You must print `DISCARD:` with the `key` discarded and followed by a new line.
- `def get(self, key)`:
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn't exist in `self.cache_data`, return `None.

These tasks will help you gain a deep understanding of caching and different eviction policies.

## How to Use

Each caching system you implement will be available as a Python class. You can create instances of these classes and use the `put` and `get` methods to store and retrieve data from the cache. Be sure to follow the specific rules and eviction policies outlined in each task.

## Repository

The code for this project can be found in the following GitHub repository:

- Repository: [alx-backend](https://github.com/tkirwa/alx-backend)
- Directory: 0x01-caching

## Authors

This project was created by [Tonny Kirwa](https://github.com/tkirwa)
