# Extract Phone Number column L named TelUpdated in L1 cell and remove the leading +91 country code
import pandas as pd


def extract_telupdated_column(excel_file_path):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(excel_file_path)

    # Extract the "TelUpdated" column as a list
    telephone_number = df['TelUpdated'].tolist()

    # Filter values that start with "91" and are not exactly "91"
    filtered_values = [value for value in telephone_number if str(value).startswith('91') and str(value) != '91']
    # Remove the "91" prefix from each value
    stripped_values = [value.lstrip('91') for value in filtered_values]

    return stripped_values
