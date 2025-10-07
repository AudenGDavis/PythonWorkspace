from typing import List, Set
# explicitly listing them
words: Set[str] = {'hi', 'hi', 'hello', 'hi', 'howdy', 'hi'}  

# using the set constructor
numbers: Set[int] = set(range(5)) 
print(numbers, end = " <= crange(5) converted to set\n")  # {0, 1, 2, 3, 4} 

list_of_floats: List[float] = [3.4, 3.2, 2.9, 3.4, 3.0]

# using the set constructor that takes an existing collection
measurements: Set[float] = set(list_of_floats)
# {3.2, 3.0, 2.9, 3.4}
print(measurements, end = " <= duplicate 3.4 removed\n")
