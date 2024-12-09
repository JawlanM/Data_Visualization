import pandas as pd

# Load the file
file_path = 'C:/Users/asany/OneDrive/Desktop/Book2.csv'
df = pd.read_csv(file_path)

# Convert the datetime column to pandas datetime
datetime_column = df.columns[0]  # Replace with your actual column name
df[datetime_column] = pd.to_datetime(df[datetime_column])

# Extract components
df['Year'] = df[datetime_column].dt.year
df['Month'] = df[datetime_column].dt.month_name()
df['Hour'] = df[datetime_column].dt.hour
df['Day'] = df[datetime_column].dt.day_name()

# Save the processed file
output_path = 'C:/Users/asany/OneDrive/Desktop/Processed_Book2.csv'
df.to_csv(output_path, index=False)

print("File saved at:", output_path)
