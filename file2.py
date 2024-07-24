from google.colab import drive
import pandas as pd

# Mount Google Drive
drive.mount('/content/drive')

# Adjust the file path to match your specific Google Drive folder structure
file_path = '/content/drive/My Drive/Colab Notebooks/fer2013.csv'

# Load the CSV file into a DataFrame
try:
    data = pd.read_csv(file_path)
    # Display first few rows to verify if data is loaded correctly
    print(data.head())
except FileNotFoundError:
    print(f'File not found at {file_path}. Please verify the file path.')
