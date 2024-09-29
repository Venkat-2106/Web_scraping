Code Overview
Imports:

Uses BeautifulSoup for web scraping, requests for fetching web content, and pandas for data manipulation.
Fetch HTML Content:

Retrieves the HTML of the specified Wikipedia page.
Parse HTML:

Parses the page using BeautifulSoup and locates the specific table of interest.
Extract Table Headers:

Grabs the headers from the table and prepares a pandas DataFrame.
Extract Table Data:

Loops through the rows of the table, extracting the data and appending it to the DataFrame.
Output:

Prints the DataFrame to the console and saves it as a CSV file.
