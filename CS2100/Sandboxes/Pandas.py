import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, 22, 32],
        'City': ['New York', 'Los Angeles', 'Chicago', 'New York']}
df = pd.DataFrame(data)

# Select rows where 'City' is 'New York'
new_york_rows = df[df['City'] == 'New York']
print(df)
print(new_york_rows)
