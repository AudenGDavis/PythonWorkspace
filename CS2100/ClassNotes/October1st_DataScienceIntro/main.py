import pandas as pd

data = {
    'title': ['The Matrix', 'Inception', 'Interstelar','Blade Runner'],
    'year': [1990, 2010,2014,1982],
    'rating' : [8.7, 8.8, 8.6, 8.1]
}

mdf: pd.DataFrame = pd.DataFrame(data)

for index, row in mdf.iterrows():
    print(f"{row['title']} scored {row['rating']}")

print(f"Average score is {mdf['rating'].mean()}")