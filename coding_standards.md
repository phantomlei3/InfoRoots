# Python Coding Standards

### Import Packages
##### Standard
- Write import statements always at the top of files.
- Import each module using the full pathname location of the module.

##### Example

```python
import numpy as np
from sklearn import linear_model
import crawler.spiders.articles   
```

### Variables
##### Standard
- Do not use global variables
- Each variable name including temporary variables should be descriptive 
##### Example
``` Python
def main():
    author_info_file_path = ".../author.csv"
    # ...
    temp_file_index = 0
```

### Functions and Methods
##### Standard
- Each name should be descriptive
- The name conventions of methods and functions are all lower cases with '_' as space
- The name conventions of attributes are all lower cases with '_' as space
- Each method and function has documentation of input and output, and descriptive comments about what does it do.
##### Example
``` Python
# Calculate the sum of two values
def sum_of_two_value(a, b):
    '''
    :params a, a integer or float
            b, a integer or float
    :returns sum, sum of a and b
    '''
    return a + b
```

### Classes
##### Standard
- The name conventions of class should be capitalized and descriptive
##### Example
``` Python
class AuthorCredibility(object):
    def __init___(self, author_name):
    ...

```

### High Cohesion Design
##### Standard
- Make sure that function is not related to its class or its python file.
- Create a new file or class for unique function
##### Example
``` python
# file name: crawling_author.py
def extract_author_info(author_name)

# file name: crawling_publisher.py
def extract_publisher_info(publisher_name)
```