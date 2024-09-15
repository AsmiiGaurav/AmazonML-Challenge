import pandas as pd
import pandas as pd

def fetch_column_to_list(file_path, column_name):
    # Read the dataset
    df = pd.read_csv(file_path)
    
    # Check if the column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the dataset.")
    
    # Fetch the content of the column and add it to a list
    column_data = df[column_name].tolist()
    
    return column_data

# Example usage
if __name__ == "__main__":
    file_path = 'dataset/train.csv'  # Replace with your dataset path
    column_name = 'image_link'        # Replace with the column you want to fetch
    
    try:
        column_list = fetch_column_to_list(file_path, column_name)
        print(column_list)
    except Exception as e:
        print(f"An error occurred: {e}")
