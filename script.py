import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)

# Add a new column
df['Salary'] = [70000, 80000, 60000, 90000, 75000]

# Filter rows where Age is greater than 25
filtered_df = df[df['Age'] > 25]

# Group by City and calculate the mean Age and Salary
grouped_df = df.groupby('City').agg({'Age': 'mean', 'Salary': 'mean'})

# Print the results
print("\nFiltered DataFrame (Age > 25):")
print(filtered_df)

print("\nGrouped DataFrame (mean Age and Salary by City):")
print(grouped_df)

print ("hello")
