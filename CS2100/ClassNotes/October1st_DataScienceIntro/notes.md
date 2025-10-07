# Data Science Intro

## Specialized Libraries 

Normal python collections (lists, tuples) are too inefficient to use for large datasets. Each elements is it's own object with it's own class. 

But in flat sequences (str, bytes, arrays) raw values are stored as elements. But every value must be the same type.

```
sensor_readings = []

for i in range(1000000):
    reading = get_sensor_data(i)
    sensor_readings.append(reading) #very inefficient 
```


### Numpy

```
import numpy as np

vector_1d = np.array([1,2,3,4,5])

matrix_2d = np.array([
    [1,2,3],
    [4,5,6])

print(f"Shape: {matrix_2d.shape}") # prints (2,3)

```

Also create array with specific pattern
```
array = np.arange(10) # [0 1 2 3 4 5 6 6 7 8 9]

rand_array = np.random.randint(10, 20, size=5) # 5 ints between 10 (inclusive) and 20 (exclusive)
```

Also can reshape:
```
a.shape = (2,3)

a.transpose()
```

Numpy supports matrix operations. Must be valid shapes.
```
v3 = v1 + v2
v3 = v1 - v2
V3 = v1 + v2
v3 = v1 / v2 # watch out for divide by zero
```

### Pandas

Means for navigating tabular data (spreadsheet)

```
pip install pandas
pip install pandas-stubs
```
#### Types
Series: one dimensional list (vector)
Data Frame: two dimensional list (matrix)

 
