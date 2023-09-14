import pandas as pd
from functionlib.nba_stats_lib import scrape_stats, repeated_headers_bball_ref

# Run for loop through the years through which we want stats
# NB: we consider year to be when the season ends (ie 16/17 season means year is 2017)
start_year = 2004
end_year = 2023

lebron_career_stats = []
for year in range(start_year, end_year+1):
    # Define the URL for LeBron James' game log for the specified year
    url = f"https://www.basketball-reference.com/players/j/jamesle01/gamelog/{year}/#pgl_basic"

    # Call the function to scrape data for required years
    lebron_stats = scrape_stats(year, url)

    lebron_stats["Year"] = year
    lebron_career_stats.append(lebron_stats)

lebron_career_stats = repeated_headers_bball_ref(lebron_career_stats)
