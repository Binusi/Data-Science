import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_stats(year, url):
    
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the table containing the game log data
        table = soup.find('table', {'id': 'pgl_basic'})
        
        if table:
            # Read the table into a Pandas DataFrame
            df = pd.read_html(str(table))[0]
            return df
        else:
            print(f"No data found for LeBron James in {year}")
    else:
        print(f"Failed to fetch data for LeBron James in {year}")

def repeated_headers_bball_ref(dataframe):
    # Combine all the data frames into one
    dataframe = pd.concat(dataframe, ignore_index=True)

    # Identify rows where the "G" column contains column names
    invalid_rows = dataframe[dataframe['G'] == 'G']

    # Find their indices and convert them to a list
    invalid_indices = invalid_rows.index.tolist()

    # Drop the invalid rows
    dataframe = dataframe.drop(invalid_indices)

    # Reset the DataFrame indices
    dataframe.reset_index(drop=True, inplace=True)

    return dataframe